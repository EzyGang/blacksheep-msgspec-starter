from blacksheep import Router

from app.apps.hello_world.api import hello_world_router


router = Router(
    sub_routers=[hello_world_router],
)
