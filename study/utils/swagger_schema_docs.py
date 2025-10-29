from drf_yasg import openapi

STUDENT_CREATE_VIEW = {
    "operation_id": "create_student",
    "operation_description": "Создание студента.",
    "operation_summary": "Создание пользователя (студента)",
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "username": openapi.Schema(type=openapi.TYPE_STRING, description="Логин пользователя"),
            "name": openapi.Schema(type=openapi.TYPE_STRING, description="Имя пользователя"),
            "email": openapi.Schema(type=openapi.TYPE_STRING, description="Электронная почта"),
            "password": openapi.Schema(type=openapi.TYPE_STRING, description="Пароль"),
            "phone_number": openapi.Schema(type=openapi.TYPE_STRING, description="Номер телефона"),
            "age": openapi.Schema(type=openapi.TYPE_INTEGER, description="Возраст"),
        },
    ),
    "responses": {
        201: openapi.Response(
            description="Данные пользователя (студента) успешно созданы",
        ),
        404: openapi.Response(
            description="Пользователь не создан",
        ),
    },
    "security": [{"Bearer": []}],  # Пример использования схемы безопасности
    "deprecated": False,  # Указывает, что данный метод не устарел
    "tags": ["User Management"],  # Теги для группировки в документации
    "extra_overrides": {"x-custom-field": "custom_value"},  # Дополнительные параметры
}

USER_GET_VIEW = {
    "operation_id": "get_user",
    "operation_description": "Получение информации о студенте по ID.",
    "operation_summary": "Получить пользователя",
    "request_body": None,
    "manual_parameters": [
        openapi.Parameter(
            "user_id",
            openapi.IN_PATH,
            description="ID студента, которого необходимо получить.",
            type=openapi.TYPE_INTEGER,
            required=True,
        )
    ],
    "responses": {
        200: openapi.Response(
            description="Успешно получен пользователь",
            schema=openapi.Schema(type=openapi.TYPE_STRING, description="Данные пользователя успешно получены"),
        ),
        404: openapi.Response(
            description="Пользователь не найден",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"detail": openapi.Schema(type=openapi.TYPE_STRING, description="Сообщение об ошибке")},
            ),
        ),
    },
    "security": [{"Bearer": []}],  # Пример использования схемы безопасности
    "deprecated": False,  # Указывает, что данный метод не устарел
    "tags": ["User Management"],  # Теги для группировки в документации
    "extra_overrides": {"x-custom-field": "custom_value"},  # Дополнительные параметры
}

ENROLLMENTS_GET_VIEW = {
    "operation_id": "get_enrollments",
    "operation_description": "Получение сведений о зачислении студентов.",
    "operation_summary": "Получить список зачислений",
    "request_body": None,  # Для GET-запроса тело не требуется
    "manual_parameters": [
        # по умолчанию запрос без path параметров, при необходимости можно добавить query параметры
    ],
    "responses": {
        200: openapi.Response(
            description="Успешно получен список зачислений студентов",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID записи о зачислении"),
                        "grade": openapi.Schema(type=openapi.TYPE_INTEGER, description="Оценка"),
                        "enroll_date": openapi.Schema(type=openapi.FORMAT_DATE, description="Дата зачисления"),
                        "student": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description="Информация о студенте",
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "name": openapi.Schema(type=openapi.TYPE_STRING),
                                "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
                                "age": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "graduation_date": openapi.Schema(type=openapi.FORMAT_DATE),
                                "created_at": openapi.Schema(type=openapi.FORMAT_DATETIME),
                                "updated_at": openapi.Schema(type=openapi.FORMAT_DATETIME),
                            },
                        ),
                        "course": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description="Информация о курсе",
                            properties={
                                # Все поля модели Course
                                # Можно повторить поля аналогично Student или просто указать
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "title": openapi.Schema(type=openapi.TYPE_STRING),
                                "teacher_name": openapi.Schema(type=openapi.TYPE_STRING),
                                # Добавить другие поля модели Course, если нужно
                            },
                        ),
                    },
                ),
            ),
        ),
        404: openapi.Response(
            description="Зачисления не найдены",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"detail": openapi.Schema(type=openapi.TYPE_STRING, description="Сообщение об ошибке")},
            ),
        ),
    },
    "security": [{"Bearer": []}],  # Для обеспечения безопасности через JWT
    "deprecated": False,
    "tags": ["Enrollment Management"],
    "extra_overrides": {"x-custom-field": "custom_value"},
}
