import json

import redis

from utils.logging_config import logger

# Подключение к Redis
cache = redis.Redis(host="localhost", port=6379, db=0)


class CacheSet:
    def __init__(self, data, key):
        self.data = json.dumps(data)
        self.key = key

    def set_data(self):
        try:
            cache.set(self.key, self.data, ex=60)
        except Exception as e:
            logger.error(f"Ошибка при записи в кеш: {e}")


class CacheGet:
    def __init__(self, key):
        self.key = key

    def get_data(self):
        try:
            data = cache.get(self.key)
            if data is None:
                return None
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            logger.error(f"Ошибка при чтении из кеша: {e}")
        return None
