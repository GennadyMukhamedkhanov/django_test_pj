from db.models import Course
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.course.get import CourseGetSerializer


class CourseSerializer:
    pass


class CourseCreate(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, **kwargs):
        course = Course(
            title=request.data.get("title"),
            teacher_name=request.data.get("teacher_name"),
            photo=request.data.get("photo"),
        )

        course.save()
        serializer = CourseGetSerializer(course).data

        return Response(serializer, status=status.HTTP_201_CREATED)


class CourseGetAllCreate(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, **kwargs):
        course = Course.objects.all()

        serializer = CourseGetSerializer(course, many=True).data

        return Response(serializer, status=status.HTTP_201_CREATED)
