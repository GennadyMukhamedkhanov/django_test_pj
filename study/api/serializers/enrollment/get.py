from db.models import Course, Enrollment, Student
from rest_framework import serializers


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = (
            "id",
            "name",
            "phone_number",
            "age",
            "graduation_date",
            "created_at",
            "updated_at",
        )


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentEnrollmentSerializer()
    course = CourseEnrollmentSerializer()

    class Meta:
        model = Enrollment

        fields = (
            "id",
            "student",
            "course",
            "grade",
            "enroll_date",
        )
