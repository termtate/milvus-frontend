from enum import Enum
from pydantic.dataclasses import dataclass

class State:
    class Loading:
        pass

    @dataclass
    class Error:
        msg: str

    @dataclass
    class Success:
        data: str
    

a = State.Loading()

match a:
    case State.Loading():
        print("l")
    case State.Error(msg=msg):
        print(f"err:{msg}")
    case State.Success(data=d):
        print(d)


