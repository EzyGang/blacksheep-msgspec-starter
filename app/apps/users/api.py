from blacksheep import Router

from app.apps.users.dtos import HelloWorld
from app.binders import FromMsgPack
from app.core.responses import MsgPackResponse

users_router = Router()
_prefix = '/api/v1/users'


@users_router.post(_prefix + '/hello-world')
async def hello_world(data: FromMsgPack[HelloWorld]) -> MsgPackResponse[HelloWorld]:
    return MsgPackResponse(data=data.value)
