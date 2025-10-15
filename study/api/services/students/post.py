from db.models import Student
from django import forms
from django.db.models import Q
from service_objects.services import Service


class StudentAdultsFilterService(Service):
    phone_number = forms.IntegerField()
    name = forms.CharField()
    age = forms.CharField()
    email = forms.EmailField()

    def process(self):
        self.check_user()
        return self._create_user

    def check_user(self):
        user = Student.objects.filter(
            Q(phone_number=self.cleaned_data['phone_number']) |
            Q(email=self.cleaned_data['email'])
        )
        if user.exists():
            raise Exception('Студент с такими данными уже существует')

    @property
    def _create_user(self):
        try:
            students = Student.objects.create_user(
                phone_number=self.cleaned_data['phone_number'],
                name=self.cleaned_data['name'],
                age=self.cleaned_data['age'],
                email=self.cleaned_data['email'],

            )
        except Exception:
            raise
        return students
