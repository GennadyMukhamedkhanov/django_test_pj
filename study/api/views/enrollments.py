from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.cache import CacheGet, CacheSet

from api.serializers.enrollment.get import EnrollmentSerializer
from api.services.enrollments.get import GetEnrollmentService
from study.utils.logging_config import logger


class EnrollmentGetView(APIView):
    def get(self, request, **kwargs):
        logger.info(
            "Запрос на получение сведений о зачислении студентов от пользователя: "
            f"id:{request.user.id} имя:{request.user.name}"
        )
        key = f"cache:{request.path.strip('/').replace('/', ':')}"
        cache = CacheGet(key)
        result = cache.get_data()
        if result is not None:
            logger.info("Даннае из кеша успешно получены ")
            return Response(result, status=status.HTTP_200_OK)

        enrollments = GetEnrollmentService.execute({})

        logger.info("Начинается сериализация данных объектов")
        serializer = EnrollmentSerializer(enrollments, many=True).data
        logger.success("Сериализация данных успешно закончена")
        cache = CacheSet(serializer, key)
        cache.set_data()
        logger.info("Даннае записаны в кеш успешно ")

        return Response(serializer, status=status.HTTP_200_OK)
