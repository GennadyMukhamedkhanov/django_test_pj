from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.enrollment.get import EnrollmentSerializer
from api.services.enrollments.get import GetEnrollmentService
from study.utils.logging_config import logger


class EnrollmentGetView(APIView):
    def get(self, request, **kwargs):
        logger.info(
            "Запрос на получение сведений о зачислении студентов от пользователя: "
            f"id:{request.user.id} имя:{request.user.name}"
        )
        enrollments = GetEnrollmentService.execute({})

        logger.info("Начинается сериализация данных объектов")
        serializer = EnrollmentSerializer(enrollments, many=True).data
        logger.success("Сериализация данных успешно закончена")

        return Response(serializer, status=status.HTTP_200_OK)
