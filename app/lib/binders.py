from typing import Any, TypeVar

import msgspec.msgpack
from blacksheep import Request
from blacksheep.server.bindings import Binder, BoundValue


T = TypeVar('T')


class FromMsgPack(BoundValue[T]):
    pass


decoder = msgspec.msgpack.Decoder()


class MsgPackBinder(Binder):
    handle = FromMsgPack

    async def get_value(self, request: Request) -> Any:
        if not (content := await request.read()):
            return None
        return msgspec.msgpack.decode(content, type=self.expected_type)
