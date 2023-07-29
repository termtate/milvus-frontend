from typing import Any, Literal
import httpx  # 或者可以使用requests
from network.model import Patient, PatientList, PatientQueryFields, AnnSearchParams, ModifyResponse, PatientCreate
# from pydantic import 
import asyncio
from pprint import pprint
from typing_extensions import Unpack

url = "http://127.0.0.1:8000/api/v1/patients"

client = httpx.Client()

def _get(url: str, params=None) -> list[Patient]:
    res = client.get(url, params=params, follow_redirects=True) # 需要加follow_redirects允许重定向
    return PatientList.model_validate_json(res.content).root

def _post(url: str, json=None) -> ModifyResponse:
    return ModifyResponse.model_validate_json(
        client.post(f"{url}/batch", json=json, follow_redirects=True).content
    )


def get_patients_by_id(id: int):
    return _get(f"{url}/{id}")

def get_patients_by_fields(
    **fields: Unpack[PatientQueryFields],
):
    return _get(url, params=fields)

def get_patients_by_ann_search(query: str, **params: Unpack[AnnSearchParams]):
    config = dict(params)
    config["query"] = query
    return _get(f"{url}/ann_search", params=params)


def delete_patients(*patients_id: int):
    return _post(f"{url}/batch", patients_id)

def create_patients(*patients: PatientCreate):
    return _post(url, [p.model_dump_json() for p in patients])

def update_patient(id: int):
    # TODO 还没有实现
    pass