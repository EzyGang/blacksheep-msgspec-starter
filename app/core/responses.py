from typing import Generic, TypeVar

import msgspec.msgpack
from blacksheep import Content, Response
from blacksheep.headers import HeaderType
from msgspec import Struct


T = TypeVar('T')
encoder = msgspec.msgpack.Encoder()


class MsgPackResponse(Generic[T], Response):
    def __init__(
        self,
        status: int = 200,
        headers: list[HeaderType] | None = None,
        data: T | None = None,
    ) -> None:
        super().__init__(
            status=status,
            headers=headers,
            content=Content(
                content_type=b'application/msgpack',
                data=encoder.encode(data),
            )
        )
