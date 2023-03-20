from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ["interface_jsons", "uuid"]
    INTERFACE_JSONS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    interface_jsons: _containers.RepeatedScalarFieldContainer[bytes]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., interface_jsons: _Optional[_Iterable[bytes]] = ...) -> None: ...
