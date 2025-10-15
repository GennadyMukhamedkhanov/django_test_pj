
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from db.models.course import Course
from db.models.student import Student


class Enrollment(models.Model):
    student = models.ForeignKey(Student,
                                related_name='enrollments',
                                on_delete=models.CASCADE,
                                verbose_name='Студент')
    course = models.ForeignKey(Course,
                               related_name='enrollments',
                               on_delete=models.CASCADE,
                               verbose_name='Курс')
    grade = models.IntegerField(null=True,
                                blank=True,
                                validators=[
                                    MinValueValidator(0),
                                    MaxValueValidator(100)],
                                verbose_name='Категория'
                                )
    enroll_date = models.DateField(verbose_name='Дата зачисления')

    class Meta:
        db_table = 'Enrollment'
        verbose_name = 'Зачисление'
        verbose_name_plural = 'Зачисление'
        db_table = 'enrollment'

    def __str__(self):
        return f'Студент: {self.student}, Курс: {self.course}, Категория: {self.grade}, Дата: {self.enroll_date}'
