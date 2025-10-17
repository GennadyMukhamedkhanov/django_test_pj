from db.models import Student
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.student.get import StudentSerializer


class StudentCreateView(APIView):
    def post(self, request, **kwargs):
        student = Student(
            phone_number="89772941215",
            name="Gena5",
            age=35,
            email="dungreshmen5@mail.ru",
            username="gennadiy5",
        )

        student.set_password("198610")  # Хеширует пароль
        student.save()
        serializer = StudentSerializer(student).data

        return Response(serializer, status=status.HTTP_200_OK)
