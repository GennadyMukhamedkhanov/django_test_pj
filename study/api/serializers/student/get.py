from db.models import Course, Enrollment, Student
from rest_framework import serializers


class CourseStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentStudentSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.title')


    class Meta:
        model = Enrollment

        fields = (
            'id',
            'course',
            'grade',
            'enroll_date',

        )


class StudentSerializer(serializers.ModelSerializer):
    count_students = serializers.SerializerMethodField()
    enrollment = serializers.SerializerMethodField()

    class Meta:
        model = Student

        fields = (
            'id',
            'name',
            'phone_number',
            'age',
            'graduation_date',
            'created_at',
            'updated_at',
            'count_students',
            'enrollment'

        )

    def get_enrollment(self, obj):
        enrollments = obj.enrollments.all()
        serializer = EnrollmentStudentSerializer(enrollments, many=True).data
        return serializer if bool(serializer) == True else None



    def get_count_students(self, obj):
        if hasattr(obj, 'count_students'):
            return obj.count_students
