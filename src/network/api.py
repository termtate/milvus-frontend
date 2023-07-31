from typing import Any, Literal
import httpx  # 或者可以使用requests
from network.model import Patient, PatientList, PatientQueryFields, AnnSearchParams, ModifyResponse
# from pydantic import 
import asyncio
from pprint import pprint
from typing_extensions import Unpack

url = "http://127.0.0.1:8000/api/v1/patients"

client = httpx.Client(timeout=20)

def _get(url: str, params=None) -> list[Patient]:
    res = client.get(url, params=params, follow_redirects=True) # 需要加follow_redirects允许重定向
    return PatientList.model_validate_json(res.content).root

def _post(url: str, json=None) -> ModifyResponse:
    r = client.post(url, json=json, follow_redirects=True, headers={"Content-Type": "application/json; charset=utf-8"})
    print(r.text)
    return ModifyResponse.model_validate_json(
        r.content
    )
    


def get_patients_by_id(id: int):
    return _get(f"{url}/{id}")

def get_patients_by_fields(
    **fields: Unpack[PatientQueryFields],
):
    return _get(url, params=fields)

def get_patients_by_ann_search(query: str, field: str, **params: Unpack[AnnSearchParams]):
    config = dict(params)
    config["query"] = query
    config["field"] = field
    return _get(f"{url}/ann_search", params=params)


def delete_patients(*patients_id: int):
    return _post(f"{url}/batch", patients_id)

def delete_all():
    return ModifyResponse.model_validate_json(client.delete(f"{url}/").content)

def create_patients(*patients: Patient):
    return _post(url, [p.model_dump() for p in patients])

def update_patient(id: int, field_name: str, value: Any):
    return client.put(f"{url}/{id}", params={"field_name": field_name, "value": value})