import sys

from loguru import logger

logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO", enqueue=True)

logger.info("=== LOGURU GLOBAL CONFIG LOADED ===")


#
# logger.add(
#     "logs/app.log",
#     level="DEBUG",
#     format="{time} | {level} | {message} | {file}:{line}",
#     rotation="10 MB",
#     retention="7 days",
#     enqueue=True,
#     backtrace=True,
#     diagnose=False,
# )
