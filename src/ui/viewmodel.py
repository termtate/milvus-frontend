import asyncio
from functools import wraps
from typing import Any, Callable, Sequence
from typing_extensions import Unpack, TypedDict
import pandas as pd
from pydantic import BaseModel
from ml.recognize import Recognizer
from common.model import Patient, PatientCreate
from reactivex.subject import BehaviorSubject
from qasync import asyncSlot, asyncClose
from injector import inject
from db.crud import CRUDPatient
from common.config import settings
from httpx._exceptions import HTTPError
import logging

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class State(BaseModel):
    """
    提供给界面的状态，界面需要根据这些数据自行渲染
    """
    is_loading: bool
    error_message: str | None  # 如果不为空，就显示弹窗
    upload_success: bool
    
    table_data: Sequence[Patient]


class StateDict(TypedDict, total=False):  # for type checking
    is_loading: bool
    error_message: str | None
    upload_success: bool
    
    table_data: Sequence[Patient]


def with_loading_state(func):
    """
    装饰器，在被装饰的函数运行时将`State`的`is_loading`值修改为True
    """
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        self._update(is_loading=True)
        res = await func(self, *args, **kwargs)
        self._update(is_loading=False)
        return res
    return wrapper

def catch_error(func):
    """
    装饰器，在被装饰的函数运行时捕获Exception，并且把Exception的字符串更新为`State`的`error_message`
    """
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            return await func(self, *args, **kwargs)
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            self._update(error_message=str(e), is_loading=False)
    
    return wrapper


def log(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"function {func.__name__} called with args {signature}")
        return func(*args, **kwargs)
    return wrapper


def with_loading_and_error(func):
    """
    装饰器，同时装饰`with_loading_state`和`catch_error`
    """
    return catch_error(
        with_loading_state(func)
    )



class ViewModel:
    @inject  # 使用inject给构造函数注入其他模块
    def __init__(self, crud_patient: CRUDPatient, recognizer: Recognizer):
        # BehaviorSubject是一个流，该流只保留最新一次的数据，
        # 所以必须要有一个初始值。
        # 流需要被其他订阅者订阅。当调用`BehaviorSubject.on_next()`方法时，
        # 所有订阅者都会被通知，即调用一次他们订阅的函数
        self.state: BehaviorSubject[State] = BehaviorSubject(
            State(
                is_loading=False,
                error_message=None,
                table_data=[],
                upload_success=False
            )
        )
        self.crud_patient = crud_patient
        self.recognizer = recognizer
        
    
    def _update(self, **values: Unpack[StateDict]):
        '''
        更新State，为了防止线程冲突，每次更新的值都必须是State的深拷贝
        '''
        self.state.on_next(
            self.state.value.model_copy(
                update=dict(values),
                deep=True
            )
        )
    
    @asyncSlot()
    @with_loading_and_error
    @log
    async def common_search(self, text: str):
        if not text:
            self._update(error_message='输入不能为空！')
            return
        if text.isdigit():
            patients = await self.crud_patient.get_patients_by_fields(field="case_number", value=text)
        else:
            patients = await self.crud_patient.get_patients_by_fields(field="name", value=text)
        self._update(table_data=patients)

    @asyncSlot()
    @with_loading_and_error
    @log
    async def advanced_search(self, query: str, field: str):
        if not query:
            self._update(error_message='输入不能为空！')
            return
        patients = await self.crud_patient.ann_search_patient(
            query=query,
            field=settings.COLUMNS_NAME_MAP[field],
            limit=10,
            offset=0
        )
        self._update(table_data=patients.data)
    
    @asyncSlot()
    @with_loading_and_error
    @log
    async def update_field(self, id: int, field: str, value: Any):
        """
        更新病人的一个字段
        """
        await self.crud_patient.update_patient_field(
            patient_id=id, field_name=settings.COLUMNS_NAME_MAP[field], value=value)
        
        items = list(self.state.value.table_data)
        for item in items:
            if item.id == id:
                
                setattr(item, settings.COLUMNS_NAME_MAP[field], value)
        
        self._update(table_data=items)
    
    
    @asyncSlot()
    @with_loading_and_error
    @log
    async def upload_file(self, path: str):
        await asyncio.to_thread(self.recognizer.read_files2, path)  # 把一个非异步函数放到一个线程去执行
        res = self.recognizer.read_files2(path)
        patients = []
        for i in res:
            i["身份证号"] = ""

            trans = {settings.COLUMNS_NAME_MAP[k]: v for k, v in i.items()}
            patients.append(trans)


        await self.crud_patient.create_patients(*[
            PatientCreate(**_) for _ in patients
        ])
        
        self._update(upload_success=True)
        
    @asyncSlot()
    @with_loading_and_error
    @log
    async def delete_patients(self, *id: int):
        await self.crud_patient.delete_patients(*id)
        
        items = list(filter(
            lambda item: item.id not in id,
            self.state.value.table_data
        ))
        
        self._update(table_data=items)


    @asyncSlot()
    @with_loading_and_error
    @log
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
        await self.crud_patient.disconnect()
    
