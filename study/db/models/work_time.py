from django.db import models

from db.models.student import Student


class WorkTime(models.Model):
    user = models.ForeignKey(Student, related_name="work_times", on_delete=models.CASCADE, verbose_name="Студент")

    date = models.DateField(verbose_name="Дата")

    hours_worked = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Отработанные часы")

    class Meta:
        db_table = "WorkTime"
        verbose_name = "Рабочее время"
        verbose_name_plural = "Рабочее время"

    def __str__(self):
        return f"Студент: {self.user}, Дата: {self.date}, Отработанные часы: {self.hours_worked}"
