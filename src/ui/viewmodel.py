import asyncio
from functools import wraps
import os
from pprint import pprint
from typing import Any, Sequence
from typing_extensions import Unpack, TypedDict
import pandas as pd
from pydantic import BaseModel, TypeAdapter
from ml.recognize import Recognizer
from network.model import Patient, PatientCreate
from reactivex.subject import BehaviorSubject
from qasync import asyncSlot, asyncClose
from injector import inject
from network.api import Client
from config import settings
from httpx._exceptions import HTTPError


class State(BaseModel):
    is_loading: bool
    error_message: str | None
    upload_success: bool
    
    table_data: Sequence[Patient]


class StateDict(TypedDict, total=False):  # for type checking
    is_loading: bool
    error_message: str | None
    upload_success: bool
    
    table_data: Sequence[Patient]


def with_loading_state(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        self._update(is_loading=True)
        res = await func(self, *args, **kwargs)
        self._update(is_loading=False)
        return res
    return wrapper

def catch_error(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            return await func(self, *args, **kwargs)
        except HTTPError as e:
            self._update(error_message=str(e), is_loading=False)
    
    return wrapper

def with_loading_and_error(func):
    return catch_error(
        with_loading_state(func)
    )



class ViewModel:
    @inject
    def __init__(self, client: Client, recognizer: Recognizer):
        self.state: BehaviorSubject[State] = BehaviorSubject(
            State(
                is_loading=False,
                error_message=None,
                table_data=[],
                upload_success=False
            )
        )
        self.client = client
        self.recognizer = recognizer
    
    
    def _update(self, **values: Unpack[StateDict]):
        self.state.on_next(
            self.state.value.model_copy(
                update=dict(values),
                deep=True
            )
        )
    
    @asyncSlot()
    @with_loading_and_error
    async def common_search(self, text: str):
        if not text:
            self._update(error_message='输入不能为空！')
            return
        if text.isdigit():
            patients = await self.client.get_patients_by_fields("case_number", value=text)
        else:
            patients = await self.client.get_patients_by_fields(field="name", value=text)
        self._update(table_data=patients)
        
    @asyncSlot()
    @with_loading_and_error
    async def advanced_search(self, query: str, field: str):
        if not query:
            self._update(error_message='输入不能为空！')
            return
        patients = await self.client.get_patients_by_ann_search(
            query=query,
            field=settings.COLUMNS_NAME_MAP[field]
        )
        self._update(table_data=patients.data)
    
    @asyncSlot()
    @with_loading_and_error
    async def update_field(self, id: int, field: str, value: Any):
        await self.client.update_patient(id=id, field_name=settings.COLUMNS_NAME_MAP[field], value=value)
        
        items = list(self.state.value.table_data)
        for item in items:
            if item.id == id:
                
                setattr(item, settings.COLUMNS_NAME_MAP[field], value)
        
        self._update(table_data=items)
    
    @asyncSlot()
    @with_loading_and_error
    async def upload_file(self, path: str):
        await asyncio.to_thread(self.recognizer.read_files2, path)
        res = self.recognizer.read_files2(path)
        patients = []
        for i in res:
            i["身份证号"] = ""

            trans = {settings.COLUMNS_NAME_MAP[k]: v for k, v in i.items()}
            patients.append(trans)


        await self.client.create_patients(*[
            PatientCreate(**_) for _ in patients
        ])
        
        # self._update()
        
    @asyncSlot()
    @with_loading_and_error
    async def delete_patients(self, *id: int):
        await self.client.delete_patients(*id)
        
        items = list(filter(
            lambda item: item.id not in id,
            self.state.value.table_data
        ))
        
        self._update(table_data=items)

    @asyncSlot()
    @with_loading_and_error
    async def export_to_excel(self, path: str, *ids: int):
        selected = filter(
            lambda x: x.id in ids,
            self.state.value.table_data
        )
        
        df = pd.DataFrame([_.model_dump() for _ in selected])
        
        df.to_excel(f"{path}/export.xlsx")
        self._update(upload_success=True)
        
    
    def on_error_dismiss(self):
        self._update(error_message=None)
    
    def uploaded_shown(self):
        self._update(upload_success=False)
    
    @asyncClose
    async def close(self, event):
        await self.client.close()
    
