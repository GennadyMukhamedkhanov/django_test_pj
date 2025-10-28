from datetime import date
from unittest.mock import Mock

import pytest
from db.models import Course, Enrollment, Student
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_enrollments(client):
    User = get_user_model()
    client = APIClient()

    user = User.objects.create_user(
        username="testuser",
        password="testpass",
        phone_number="89772223355",
        email="test_mail",
        age=25,
    )
    user.name = "TestName"
    user.save()

    # Создаём тестовые данные: курс и зачисление
    course = Course.objects.create(title="Test Course", teacher_name="Test teacher_name")
    Enrollment.objects.create(
        student=user,
        course=course,
        enroll_date=date.today(),  # Добавь дату зачисления
    )
    # Создаём JWT токен
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Передаём токен в заголовке
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    response = client.get(reverse("enrollments"))
    assert response.status_code == 200


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


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def user(db):
    # Создаём тестового пользователя, можно указать нужные поля
    return Student.objects.create_user(
        phone_number="89998887711",
        name="Test name student",
        age=100,
        email="teststudent11@email.ru",
        username="username_test_student11",
        password="testpass",
    )


def test_get_enrollment_view(mocker, apiclient, user, enrollment):
    # Мокаем delay задачу Celery
    mocker.patch("study.api.tasks.my_task.delay")

    # Мокаем кэш — возвращаем None, чтобы тест проходил через сервис и сериализацию
    mocker.patch("study.utils.cache.CacheGet.get_data", return_value=None)
    mocker.patch("study.utils.cache.CacheSet.set_data")

    mock_enrollment_1 = Mock(spec=["student", "course", "grade", "enroll_date"])
    mock_enrollment_1.student = Mock()  # можно настроить атрибуты студента при необходимости
    mock_enrollment_1.course = Mock()  # можно настроить атрибуты курса
    mock_enrollment_1.grade = 85
    mock_enrollment_1.enroll_date = date(2025, 10, 1)

    mock_enrollment_2 = Mock(spec=["student", "course", "grade", "enroll_date"])
    mock_enrollment_2.student = Mock()
    mock_enrollment_2.course = Mock()
    mock_enrollment_2.grade = 90
    mock_enrollment_2.enroll_date = date(2025, 10, 10)

    mock_enrollments = [mock_enrollment_1, mock_enrollment_2]
    # Мокаем сервис, чтобы вернуть подготовленные данные
    mocker.patch("study.api.services.enrollments.get.GetEnrollmentService.process", return_value=mock_enrollments)
    # Мокаем сериализацию (если нужно)
    mocker.patch(
        "study.api.serializers.enrollment.get.EnrollmentSerializer",
        return_value=Mock(data=[{"name": "Vasia", "age": 20}, {"name": "Kolia", "age": 18}]),
    )
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Передаём токен в заголовке
    apiclient.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    # Вызов view через client (с токеном, если надо)
    url = reverse("enrollments")
    print(f"Resolved URL: {url}")
    response = apiclient.get(url)

    assert response.status_code == 200
