from blacksheep import Router

from app.apps.hello_world.dtos import HelloWorld
from app.lib.binders import FromMsgPack
from app.lib.responses import MsgPackResponse


hello_world_router = Router()
_prefix = '/api/v1/users'


@hello_world_router.post(_prefix + '/hello-world')
async def hello_world(data: FromMsgPack[HelloWorld]) -> MsgPackResponse[HelloWorld]:
    return MsgPackResponse(data=data.value)
