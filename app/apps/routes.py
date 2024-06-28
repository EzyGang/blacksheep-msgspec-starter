from blacksheep import Router

from app.apps.users.api import users_router


router = Router(
    sub_routers=[users_router],
)
