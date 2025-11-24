from db.models import Course
from rest_framework import serializers


class CourseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

        fields = (
            "id",
            "title",
            "teacher_name",
            "photo",
        )
