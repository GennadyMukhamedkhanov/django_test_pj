
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса')
    teacher_name = models.CharField(max_length=100, verbose_name='Имя преподавателя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')

    class Meta:
        db_table = 'Course'
        verbose_name = 'Кукс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'Название курса: {self.title}, Имя преподавателя: {self.teacher_name}'
