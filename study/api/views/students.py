from permissions.is_author import IsAuthor
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.student.get import StudentSerializer
from api.services.students.get import GetStudentService
from study.utils.logging_config import logger


class StudentView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request, **kwargs):
        logger.info(
            f"Получен запрос на получение студента id: {kwargs.get('id')} пользователем: "
            f"id: {request.user.id} имя:{request.user.name}"
        )
        student = GetStudentService.execute(
            {
                "id": kwargs.get("id"),
            }
        )

        self.check_object_permissions(request=request, obj=student)

        logger.info(f"Начинается сериализация данных объекта - id: {student.id} {student}")
        serializer = StudentSerializer(student).data
        logger.success(f"Сериализация данных успешно закончена - student: {serializer}")

        return Response(serializer, status=status.HTTP_200_OK)
