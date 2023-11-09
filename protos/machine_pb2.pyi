from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MakeCocktailRequest(_message.Message):
    __slots__ = ["steps"]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: str
    def __init__(self, steps: _Optional[str] = ...) -> None: ...

class MakeCocktailResponse(_message.Message):
    __slots__ = ["success", "message"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
