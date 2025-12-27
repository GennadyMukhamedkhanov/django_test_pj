import logging
import os
from datetime import timedelta

from celery import Celery
from loguru import logger as loguru_logger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

app = Celery("conf")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.worker_hijack_root_logger = False

# Убираем стандартные handlers loguru и добавляем наши
loguru_logger.remove()
loguru_logger.add(
    "logs/app.log",
    level="DEBUG",
    format="{time} | {level} | {message} | {file}:{line}",
    rotation="10 MB",
    retention="7 days",
    enqueue=True,
)


# InterceptHandler
class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = loguru_logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        loguru_logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


# Подключаем к Celery логгеру
@app.on_after_configure.connect
def setup_celery_logger(**kwargs):
    celery_logger = logging.getLogger("celery")
    celery_logger.handlers = [InterceptHandler()]
    celery_logger.propagate = False


app.conf.beat_schedule = {
    "print an tasks every minute": {
        "task": "api.tasks.print_task_1_min",
        "schedule": timedelta(minutes=1),
    },
    "every": {
        "task": "myapp.tasks.print_task_30_sec",
        "schedule": timedelta(seconds=30),
    },
}
