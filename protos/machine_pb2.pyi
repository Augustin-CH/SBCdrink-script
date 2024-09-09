from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MakeCocktailRequest(_message.Message):
    __slots__ = ["steps", "dispenser_emptying_time", "dispenser_filling_time"]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    DISPENSER_EMPTYING_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPENSER_FILLING_TIME_FIELD_NUMBER: _ClassVar[int]
    steps: str
    dispenser_emptying_time: int
    dispenser_filling_time: int
    def __init__(self, steps: _Optional[str] = ..., dispenser_emptying_time: _Optional[int] = ..., dispenser_filling_time: _Optional[int] = ...) -> None: ...

class MakeCocktailResponse(_message.Message):
    __slots__ = ["success", "message"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
