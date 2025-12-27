from django.utils.deprecation import MiddlewareMixin
from utils.logging_config import logger


class SimpleMiddleware(MiddlewareMixin):  # ✅ Наследуйтесь от MiddlewareMixin!
    def process_request(self, request):  # ✅ process_request (НЕ __call__)
        logger.info(f"Запрос (в middleware) {request.method} {request.get_full_path()}")

    def process_response(self, request, response):  # ✅ process_response
        logger.info(f"Ответ (в middleware) {response.status_code} {request.get_full_path()}")
        return response
