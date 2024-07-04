import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


env_file = os.getenv('GUNICORN_ENV_FILE', '.env')


class EnvironSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file,
    )

    WEB_CONCURRENCY: int = Field(default=4, ge=0)

    HOST: str = Field(default='0.0.0.0')
    PORT: int = Field(default=8000)
    LOG_LEVEL: str = Field(default='info')

    ACCESS_LOG: str = Field(default='-')
    ERROR_LOG: str = Field(default='-')

    GRACEFUL_TIMEOUT: int = Field(default=60, ge=0)
    WORKER_CONNECTIONS: int = Field(default=10000, ge=0)
    MAX_WORKER_REQUESTS: int = Field(default=2500, ge=0)
    MAX_WORKER_REQUESTS_JITTER: int = Field(default=500, ge=0)
    TIMEOUT: int = Field(default=60, ge=0)
    KEEP_ALIVE: int = Field(default=15, ge=0)
    BACKLOG: int = Field(default=0, ge=0)


_settings = EnvironSettings()

# Gunicorn config variables
loglevel = _settings.LOG_LEVEL
workers = _settings.WEB_CONCURRENCY
bind = f'{_settings.HOST}:{_settings.PORT}'
worker_tmp_dir = '/dev/shm'
errorlog = _settings.ERROR_LOG or None
accesslog = _settings.ACCESS_LOG or None

graceful_timeout = _settings.GRACEFUL_TIMEOUT
worker_connections = _settings.WORKER_CONNECTIONS
max_requests = _settings.MAX_WORKER_REQUESTS
max_requests_jitter = _settings.MAX_WORKER_REQUESTS_JITTER
timeout = _settings.TIMEOUT
keepalive = _settings.KEEP_ALIVE
backlog = _settings.BACKLOG
