import pytest
from db.models import Course, Enrollment, Student
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers.student.get import StudentSerializer

params = (
    {
        "phone_number": "89997775533",
        "name": "test_name",
        "age": 25,
        "email": "test@email.ru",
        "username": "test_username",
    },
    {
        "phone_number": "89997775555",
        "name": "test_name2",
        "age": 30,
        "email": "test2@email.ru",
        "username": "test_username2",
    },
    {
        "phone_number": "89997775511",
        "name": "test_name3",
        "age": 33,
        "email": "test3@email.ru",
        "username": "test_username3",
    },
)


@pytest.fixture(params=params)
def data_student(request):
    return request.param


# Основной тест
@pytest.mark.django_db
def test_create_student(client, data_student):
    # Получаем URL для API, который будет тестироваться
    url = reverse("student-create")

    # Отправляем POST-запрос с данными студента
    response = client.post(url, data_student)

    # Проверяем статус ответа
    assert response.status_code == status.HTTP_201_CREATED

    assert Student.objects.count() == 1
    student = Student.objects.first()  # Получаем созданный объект Студента
    assert student.phone_number == data_student["phone_number"]
    assert student.name == data_student["name"]
    assert student.age == data_student["age"]
    assert student.email == data_student["email"]
    assert student.username == data_student["username"]


@pytest.fixture
def course():
    return Course.objects.create(
        title="Тестовое название курса",
        teacher_name="Тестовое имя преподавателя",
    )


@pytest.fixture
def student():
    return Student.objects.create(
        phone_number="89998887766",
        name="Test name student",
        age=100,
        email="teststudent@email.ru",
        username="username_test_student",
    )


@pytest.fixture
def enrollment(course, student):
    return Enrollment.objects.create(student=student, course=course, grade=55, enroll_date="2025-02-11")


@pytest.mark.django_db
def test_serializer_student(student, enrollment, course):
    serializer = StudentSerializer(student).data

    assert serializer["name"] == "Test name student"
    assert serializer["phone_number"] == "89998887766"
    assert serializer["age"] == 100
    assert serializer["count_students"] is None  # если такого свойства нет у объекта
    assert serializer["enrollment"] is not None
    assert isinstance(serializer["enrollment"], list)
    assert serializer["enrollment"][0]["course"] == course.title
    assert serializer["enrollment"][0]["grade"] == enrollment.grade
    assert serializer["enrollment"][0]["enroll_date"] == enrollment.enroll_date


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.mark.django_db
def test_get_student(apiclient, student):
    refresh = RefreshToken.for_user(student)
    access_token = str(refresh.access_token)

    # Передаём токен в заголовке
    apiclient.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    response = apiclient.get(reverse("student-detail", kwargs={"id": student.id}))
    assert response.status_code == 200
