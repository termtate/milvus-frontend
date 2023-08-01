from pydantic.dataclasses import dataclass
from typing import Literal, TypedDict
from pydantic import RootModel, BaseModel, ConfigDict
from typing_extensions import Required


class Patient(BaseModel):
    id: int
    id_card_number: str
    name: str
    hospitalize_num: str
    case_number: str
    sex: str
    age: str
    phone_number: str
    seizure_evolution: str
    seizure_duration: str
    seizure_freq: str
    maternal_pregnancy_age: str
    pregnancy_num: str
    birth_weight: str
    head_c: str
    blood_urine_screening: str
    copper_cyanin: str
    csf: str
    genetic_test: str
    head_ct: str
    head_mri: str
    scalp_eeg: str
    precipitating_factor: str


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