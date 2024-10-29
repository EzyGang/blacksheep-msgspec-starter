from typing import Any, TypeVar

from blacksheep import Request
from blacksheep.server.bindings import Binder, BoundValue
from blacksheep.settings.json import json_settings
from msgspec.json import Decoder as JSONDecoder
from msgspec.msgpack import Decoder, decode


T = TypeVar('T')


class FromMsgPack(BoundValue[T]):
    pass


decoder = Decoder()


class MsgPackBinder(Binder):
    handle = FromMsgPack

    async def get_value(self, request: Request) -> Any:
        if not (content := await request.read()):
            return None

        return decode(content, type=self.expected_type)


json_decoder = JSONDecoder()


json_settings.use(  # type: ignore[no-untyped-call]
    loads=json_decoder.decode,
)
