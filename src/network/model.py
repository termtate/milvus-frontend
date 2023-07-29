from pydantic.dataclasses import dataclass
from typing import Literal, TypedDict
from pydantic import RootModel, BaseModel
from typing_extensions import Required


class PatientBase(BaseModel):
    id_card_number: str
    hospitalize_num: str
    name: str
    
    case_number: str
    sex: Literal["男", "女"]
    age: str
    phone_number: str
    seizure_evolution: str


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int
    
class PatientList(RootModel):
    root: list[Patient]


class AnnSearchParams(TypedDict, total=False):
    limit: int  # 10 by default


class PatientQueryFields(TypedDict, total=False):
    id_card_number: str
    name: str
    hospitalize_num: str
    case_number: int
    sex: Literal["男", "女"]
    age: str 
    phone_number: str
    
class ModifyResponse(BaseModel):
    insert_count: int
    delete_count: int
    upsert_count: int
    timestamp: int
    succ_count: int
    err_count: int