from typing import Any, Literal
import httpx  # 或者可以使用requests
from network.model import Patient, PatientList, PatientQueryFields, AnnSearchParams
# from pydantic import 
import asyncio
from pprint import pprint
from typing_extensions import Unpack

url = "http://127.0.0.1:8000/api/v1/patients"

def _get(url: str, params=None) -> list[Patient]:
    res = httpx.get(url, params=params, follow_redirects=True) # 需要加follow_redirects允许重定向
    return PatientList.model_validate_json(res.content).root


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

