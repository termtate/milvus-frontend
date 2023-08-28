import asyncio
from typing import Any, Callable, ParamSpec, TypeVar, Coroutine
from db.proxy import CollectionProxy
from common.model import Patient, PatientCreate
from common.config import settings
from db.session import Session


T = TypeVar("T")
P = ParamSpec("P")
def to_async(func: Callable[P, T]) -> Callable[P, Coroutine[Any, Any, T]]:
    '''
    将一个函数转为异步函数，这个异步函数将在一个新线程运行
    '''
    async def wrapper(*args: P.args, **kwargs: P.kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper


class CRUDPatient:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.collection = session.collection
        
    
    @to_async
    def get_patient_by_id(self, *, id: int) -> list[dict[str, Any]]:
        return self.collection.query("id", id)
    
    
    @to_async
    def get_patients_by_fields(
        self,
        *, 
        field: str,
        value: Any
    ) -> list[dict[str, Any]]:
        return self.collection.query(field, value)
    
    
    @to_async
    def create(self,  *patients: PatientCreate):        
        r = self.collection.ann_insert([_.model_dump() for _ in patients])

        self.collection.flush()

        return r
    
    
    @to_async
    def ann_search_patient(self, query: str, field: str, limit: int, offset: int):
        return {
            "data": self.collection.ann_search(
                query=query,
                search_config={
                    "anns_field": field,
                    "param": settings.milvus.VECTOR_FIELD_INDEX_PARAMS,
                    "limit": limit,
                    "offset": offset
                },
            ),
            "limit": limit,
            "offset": offset
        }
    
    @to_async
    def delete_patients(
        self, 
        *id: int
    ):
        return self.collection.delete(*id)
    
    
    @to_async
    def update_patient_field(
        self, 
        patient_id: int, 
        field_name: str, 
        value: Any
    ):
        return self.collection.update(id=patient_id, field=field_name, value=value)

    @to_async
    def disconnect(self):
        self.collection.release()
        self.session.connection.disconnect()
