from functools import wraps
from typing import Any, Sequence
from typing_extensions import Unpack, TypedDict
from pydantic import BaseModel
from network.model import Patient
from reactivex.subject import BehaviorSubject
from qasync import asyncSlot, asyncClose
from injector import inject
from network.api import Client
from config import settings


class State(BaseModel):
    is_loading: bool
    error_message: str | None
    
    table_data: Sequence[Patient]


class StateDict(TypedDict, total=False):
    is_loading: bool
    error_message: str | None
    
    table_data: Sequence[Patient]
    

class ViewModel:
    @inject
    def __init__(self, client: Client):
        self.state: BehaviorSubject[State] = BehaviorSubject(
            State(
                is_loading=False,
                error_message=None,
                table_data=[],
        
            )
        )
        self.client = client
        
    
    def _update(self, **values: Unpack[StateDict]):
        self.state.on_next(
            self.state.value.model_copy(
                update=dict(values),
                deep=True
            )
        )
    
    @staticmethod
    def with_loading_state(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            self._update(is_loading=True)
            res = await func(self, *args, **kwargs)
            self._update(is_loading=False)
            return res
        return wrapper
    
    @asyncSlot()
    @with_loading_state
    async def common_search(self, text: str):
        if not text:
            self._update(error_message='输入不能为空！')
            return
        patients = await self.client.get_patients_by_id(int(text))
        self._update(table_data=patients)
        
    @asyncSlot()
    @with_loading_state
    async def advanced_search(self, query: str, field: str):
        if not query:
            self._update(error_message='输入不能为空！')
            return
        patients = await self.client.get_patients_by_ann_search(
            query=settings.COLUMNS_NAME_MAP[query],
            field=field
        )
        self._update(table_data=patients)
    
    @asyncSlot()
    @with_loading_state
    async def update_field(self, id: int, field: str, value: Any):
        await self.client.update_patient(id=id, field_name=settings.COLUMNS_NAME_MAP[field], value=value)
        
        items = list(self.state.value.table_data)
        for item in items:
            if item.id == id:
                setattr(item, settings.COLUMNS_NAME_MAP[field], value)
        
        self._update(table_data=items)
    
    
    
    def on_error_dismiss(self):
        self._update(error_message=None)
    
    @asyncClose
    async def close(self, event):
        await self.client.close()
        


    
