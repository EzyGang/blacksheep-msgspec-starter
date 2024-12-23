from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # to override info:
    # export app_info='{"title": "x", "version": "0.0.2"}'
    title: str = 'blacksheep-starter'
    version: str = '0.0.1'

    is_debug: bool = True
    log_level: str = 'INFO'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


@lru_cache
def load_settings() -> Settings:
    return Settings()
