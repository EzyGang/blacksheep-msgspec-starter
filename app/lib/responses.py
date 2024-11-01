from typing import Generic, TypeVar

import msgspec.msgpack
from blacksheep import Content, Response


T = TypeVar('T')
encoder = msgspec.msgpack.Encoder()
json_encoder = msgspec.json.Encoder()


class MsgPackResponse(Generic[T], Response):
    def __init__(
        self,
        status: int = 200,
        headers: list[tuple[bytes, bytes]] | None = None,
        data: T | None = None,
    ) -> None:
        super().__init__(
            status=status,
            headers=headers,
            content=Content(
                content_type=b'application/msgpack',
                data=encoder.encode(data),
            ),
        )


class JSONResponse(Generic[T], Response):
    def __init__(
        self,
        status: int = 200,
        headers: list[tuple[bytes, bytes]] | None = None,
        data: T | None = None,
    ) -> None:
        super().__init__(
            status=status,
            headers=headers,
            content=Content(
                content_type=b'application/json',
                data=json_encoder.encode(data),
            ),
        )
