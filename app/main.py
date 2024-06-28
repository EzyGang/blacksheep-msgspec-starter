from blacksheep import Application

from app.apps.routes import router
from app.core.auth import configure_authentication
from app.core.errors import configure_error_handlers
from app.core.settings import Settings, load_settings


def configure_application(
    settings: Settings,
) -> Application:
    _app = Application(services=None, show_error_details=settings.app.show_error_details, router=router)

    configure_error_handlers(_app)
    configure_authentication(_app, settings)
    return _app


app = configure_application(settings=load_settings())
