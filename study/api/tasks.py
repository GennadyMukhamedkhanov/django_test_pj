from celery import shared_task
from loguru import logger


@shared_task(queue="queue1")
def print_task_1_min():
    logger.info("Выполняется задача - print_task_1_min")


@shared_task(queue="queue1")
def print_task_30_sec():
    logger.info("Выполняется задача - print_task_30_sec")


@shared_task(queue="queue1")
def my_task():
    logger.info("Задача my_task запущена!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
