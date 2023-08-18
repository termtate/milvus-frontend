from pydantic import BaseModel, TypeAdapter
from typing import Literal
from abc import ABC

class Data(BaseModel):
    text: str  # 文本内容
    box: list[tuple[int, int]]  # 文本包围盒，长度为4的数组，分别为左上角、右上角、右下角、左下角的[x,y]
    score: float  # 识别置信度


class Success(BaseModel):
    code: Literal[100]
    data: list[Data]

class Error(BaseModel):
    code: Literal[101, 200, 202]  # TODO
    data: str

RecognizeResult = TypeAdapter(Success | Error)
