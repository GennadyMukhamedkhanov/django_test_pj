from api.serializers.course.get import CourseGetSerializer
from db.models import Course
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


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
            video=request.data.get("video"),
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


class CourseDelAllCreate(APIView):
    permission_classes = [
        AllowAny,
    ]

    def delete(self, request, **kwargs):
        Course.objects.all().delete()

        return Response(status=status.HTTP_200_OK)
