from db.models import Student
from django import forms
from django.shortcuts import get_object_or_404
from service_objects.services import Service


class GetStudentService(Service):
    id = forms.IntegerField(required=True)

    def process(self):
        # Здесь валидация поля id вызовется автоматически
        return self.get_user()

    def get_user(self):
        return get_object_or_404(Student, id=self.cleaned_data["id"])
