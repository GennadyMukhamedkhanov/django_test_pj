from django import forms
from permissions.is_author import IsAuthor
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.pagination import CustomPagination

from api.serializers.student.get import StudentSerializer
from api.services.students.get import GetStudentService


class StudentView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request, **kwargs):
        student = GetStudentService.execute(
            {
                "id": kwargs.get("id"),
            }
        )

        self.check_object_permissions(request=request, obj=student)

        serializer = StudentSerializer(student).data

        return Response(serializer, status=status.HTTP_200_OK)


class StudentGetView(APIView):
    def get(self, request, **kwargs):
        try:
            students = GetStudentService.execute({})
        except forms.ValidationError as e:
            raise ValidationError(str(e))

        paginator = CustomPagination()
        if request.query_params.get("page_size"):
            paginator.page_size = request.query_params.get("page_size")
        paginator_students = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(paginator_students, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)
