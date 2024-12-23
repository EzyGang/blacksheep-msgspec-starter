import asyncio
from logging import Handler, Logger, LogRecord, getLogger
from logging.config import dictConfig
from logging.handlers import QueueHandler, QueueListener
from queue import SimpleQueue as Queue

from app.core.settings import load_settings


settings = load_settings()
log_level = settings.log_level


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': log_level,
        'handlers': [
            'console',
        ],
    },
    'formatters': {
        'verbose': {'format': '[%(levelname)s] %(asctime)s %(module)s %(message)s'},
    },
    'handlers': {
        'console': {'level': log_level, 'class': 'logging.StreamHandler', 'formatter': 'verbose'},
    },
    'loggers': {
        'charset_normalizer': {
            'level': 'INFO',
            'handlers': [],
            'propagate': False,
        },
    },
}


class LocalQueueHandler(QueueHandler):
    def emit(self, record: LogRecord) -> None:
        # Removed the call to self.prepare(), handle task cancellation
        try:
            self.enqueue(record)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            print(f'LocalQueueHandler exception occurred: {e}')
            self.handleError(record)


def setup_logging_queue() -> None:
    """Move log handlers to a separate thread.

    Replace handlers on the root logger with a LocalQueueHandler,
    and start a logging.QueueListener holding the original
    handlers.

    """
    queue: Queue[LogRecord] = Queue()
    root: Logger = getLogger()

    handlers: list[Handler] = []

    handler: LocalQueueHandler = LocalQueueHandler(queue)
    root.addHandler(handler)
    for h in root.handlers[:]:
        if h is not handler:
            root.removeHandler(h)
            handlers.append(h)

    listener: QueueListener = QueueListener(queue, *handlers, respect_handler_level=True)
    listener.start()


dictConfig(LOGGING)
setup_logging_queue()


def get_logger(name: str) -> Logger:
    return getLogger(name)
