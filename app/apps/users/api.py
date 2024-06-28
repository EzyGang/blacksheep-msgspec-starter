from blacksheep import Router

from app.apps.users.dtos import HelloWorld
from app.core.responses import MsgPackResponse
from app.lib.binders import FromMsgPack


users_router = Router()
_prefix = '/api/v1/users'


@users_router.post(_prefix + '/hello-world')
async def hello_world(data: FromMsgPack[HelloWorld]) -> MsgPackResponse[HelloWorld]:
    return MsgPackResponse(data=data.value)
