from db.models import Student
from django import forms
from django.db import models
from django.db.models import Value
from service_objects.services import Service


class GetStudentService(Service):
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)

    def process(self):
        return self._get_student

    @property
    def _get_student(self):
        all_stud = Student.objects.all().count()
        students = Student.objects.annotate(
            count_students=Value(all_stud, output_field=models.IntegerField())
        )

        return students
