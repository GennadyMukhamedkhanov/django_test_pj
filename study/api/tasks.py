from celery import shared_task
from utils.logging_config import logger


@shared_task(queue="queue1")
def my_task():
    logger.info("Задача my_task запущена!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
