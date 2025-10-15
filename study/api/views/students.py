from django import forms
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.student.get import StudentSerializer
from api.services.students.get import GetStudentService


class StudentView(APIView):

    def get(self, request, **kwargs):
        student = GetStudentService.execute(
            {
                'id': kwargs.get('id'),

            }
        )
        serializer = StudentSerializer(student).data

        return Response(serializer, status=status.HTTP_200_OK)


class StudentGetView(APIView):
    def get(self, request, **kwargs):
        try:
            students = GetStudentService.execute({})
        except forms.ValidationError as e:
            raise DRFValidationError(str(e))

        serializer = StudentSerializer(students, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)
