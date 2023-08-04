from typing import Any, Type, TypeVar, Callable, Coroutine, ParamSpec
import httpx 
from network.model import Patient, PatientQueryFields, AnnSearchParams, ModifyResponse
# from pydantic import 
from typing_extensions import Unpack
import functools
from pydantic import TypeAdapter
from collections.abc import Coroutine

url = "http://127.0.0.1:8000/api/v1/patients"


T = TypeVar("T")
P = ParamSpec("P")

def _serializer(
    model: Type[T]
) -> Callable[[Callable[P, Coroutine[Any, Any, httpx.Response]]], Callable[P, Coroutine[Any, Any, T]]]:
    def inner(func: Callable[P, Coroutine[Any, Any, httpx.Response]]):
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            
            return TypeAdapter(model).validate_json((await func(*args, **kwargs)).content)
        return wrapper
    return inner


class Client:
    def __init__(self):
        self._client = httpx.AsyncClient(timeout=20, follow_redirects=True)
    
    
    @_serializer(list[Patient])
    async def get_patients_by_id(self, id: int):
        return await self._client.get(f"{url}/{id}")
    
    @_serializer(list[Patient])
    async def get_patients_by_fields(self, **fields: Unpack[PatientQueryFields],):
        return await self._client.get(url, params=fields) # type: ignore
    
    @_serializer(list[Patient])
    async def get_patients_by_ann_search(
        self, 
        query: str, 
        field: str, 
        **params: Unpack[AnnSearchParams]
    ):
        config = dict(params)
        config["query"] = query
        config["field"] = field
        return await self._client.get(f"{url}/ann_search", params=config) # type: ignore
    
    @_serializer(ModifyResponse)
    async def delete_patients(self, *patients_id: int):
        return await self._client.post(f"{url}/batch", json=patients_id)
    
    @_serializer(ModifyResponse)
    async def delete_all_patients(self):
        return await self._client.delete(url)
    
    @_serializer(ModifyResponse)
    async def create_patients(self, *patients: Patient):
        return await self._client.post(url, json=[p.model_dump() for p in patients])
    
    @_serializer(ModifyResponse)
    async def update_patient(self, id: int, field_name: str, value: Any):
        return await self._client.put(f"{url}/{id}", params={"field_name": field_name, "value": value})
    
    async def close(self):
        return await self._client.aclose()
        
