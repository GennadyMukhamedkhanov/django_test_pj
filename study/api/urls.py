from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.enrollments import By, EnrollmentGetView, Hello
from api.views.student import StudentCreateView
from api.views.students import StudentView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Получение токена
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Обновление токена
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),  # Проверка токена
    path("students/<int:id>/", StudentView.as_view(), name="student-detail"),
    path("student/", StudentCreateView.as_view(), name="student-create"),
    path("enrollment/", EnrollmentGetView.as_view(), name="enrollments"),
    path("hello/", Hello.as_view(), name="hello"),
    path("by/", By.as_view(), name="by"),
]
