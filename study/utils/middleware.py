from utils.logging_config import logger


class SimpleMiddleware:
    def __init__(self, get_response):
        # get_response — следующий шаг в цепочке (следующий middleware или сам view)
        self.get_response = get_response
        # инициализация, вызывается единожды при старте

    def __call__(self, request):
        # Код, выполняющийся до view и следующего middleware
        logger.info(f"Запрос (в middleware) {request.method} {request.get_full_path()}")

        response = self.get_response(request)  # вызов следующего слоя

        # Код, выполняющийся после view
        logger.info(f"Ответ (в middleware) {response.status_code} {request.get_full_path()}")

        return response
