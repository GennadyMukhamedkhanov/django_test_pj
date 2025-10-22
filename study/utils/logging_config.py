from loguru import logger

logger.add(
    "logs/app.log",
    level="DEBUG",
    format="{time} | {level} | {message} | {file}:{line}",
    rotation="10 MB",
    retention="7 days",
    enqueue=True,
    backtrace=True,
    diagnose=False,
)
