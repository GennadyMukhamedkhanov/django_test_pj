from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from db.models.manager import CustomUserManager


class Student(AbstractUser):
    phone_validator = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Номер телефона должен быть в формате: "
                "'+999999999'. Должно быть от 9 до 15 цифр.",
    )
    # Поле для уникального номера телефона
    phone_number = models.CharField(
        max_length=15,
        validators=[phone_validator],
        blank=False,
        null=False,
        unique=True,
        verbose_name="Телефон",
    )
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    graduation_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания учебы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обнавления')
    username = models.CharField(max_length=100, unique=False, default='us')

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "email"]
    objects = CustomUserManager()

    class Meta:
        db_table = 'Student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        db_table = 'student'


    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'
