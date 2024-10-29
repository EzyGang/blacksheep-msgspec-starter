from blacksheep import Application

from app.core.settings import Settings, load_settings
from app.main import configure_application


def test_settings_return_settings() -> None:
    assert isinstance(load_settings(), Settings)


def test_configure_application() -> None:
    assert isinstance(configure_application(load_settings()), Application)
