from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class APIInfo(BaseModel):
    title: str = 'blacksheep-starter'
    version: str = '0.0.1'


class App(BaseModel):
    show_error_details: bool = True


class Site(BaseModel):
    copyright: str = 'Example'


class Settings(BaseSettings):
    # to override info:
    # export app_info='{"title": "x", "version": "0.0.2"}'
    info: APIInfo = APIInfo()

    # to override app:
    # export app_app='{"show_error_details": True}'
    app: App = App()

    model_config = SettingsConfigDict(env_prefix='APP_')


@lru_cache
def load_settings() -> Settings:
    return Settings()
