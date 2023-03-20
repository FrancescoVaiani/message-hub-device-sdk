from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigMessage(_message.Message):
    __slots__ = ["credentials_secret", "device_id", "pairing_token", "pairing_url", "realm"]
    CREDENTIALS_SECRET_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PAIRING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAIRING_URL_FIELD_NUMBER: _ClassVar[int]
    REALM_FIELD_NUMBER: _ClassVar[int]
    credentials_secret: str
    device_id: str
    pairing_token: str
    pairing_url: str
    realm: str
    def __init__(self, realm: _Optional[str] = ..., device_id: _Optional[str] = ..., credentials_secret: _Optional[str] = ..., pairing_url: _Optional[str] = ..., pairing_token: _Optional[str] = ...) -> None: ...
