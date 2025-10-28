from db.models import Student
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.student.get import StudentSerializer


class StudentCreateView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, **kwargs):
        student = Student(
            phone_number=request.data.get("phone_number"),
            name=request.data.get("name"),
            age=request.data.get("age"),
            email=request.data.get("email"),
            username=request.data.get("username"),
        )

        student.set_password(request.data.get("password"))  # Хеширует пароль
        student.save()
        serializer = StudentSerializer(student).data

        return Response(serializer, status=status.HTTP_201_CREATED)
