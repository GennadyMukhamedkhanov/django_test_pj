from db.models import Student
from django import forms
from django.shortcuts import get_object_or_404
from service_objects.services import Service

from study.utils.logging_config import logger


class GetStudentService(Service):
    id = forms.IntegerField(required=True)

    def process(self):
        logger.debug(f"Происходит валидация данных в сервисной части- {self.cleaned_data}")
        return self.get_user()

    def get_user(self):
        try:
            student = get_object_or_404(Student, id=self.cleaned_data["id"])
            logger.info(f"Пользователь с id: {self.cleaned_data['id']} успешно получен в сервисной части")
        except Exception as e:
            logger.exception(
                f"Произошла ошибка {e} при получении пользователя с id: {self.cleaned_data['id']} в сервисной части"
            )
            raise
        return student
