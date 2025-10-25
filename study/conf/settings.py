import os
from datetime import timedelta
from pathlib import Path

import environ
from kombu import Exchange, Queue

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", cast=str)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api.apps.ApiConfig",
    "db.apps.DbConfig",
    "rest_framework",
    "service_objects",
    "rest_framework_simplejwt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "study.utils.middleware.SimpleMiddleware",
]

ROOT_URLCONF = "conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conf.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = env("STATIC_URL", cast=str, default="/static/")
STATIC_ROOT = env("STATIC_ROOT", cast=str, default=os.path.join(BASE_DIR, "static/"))

MEDIA_URL = env("MEDIA_URL", cast=str, default="/uploads/")
MEDIA_ROOT = env("MEDIA_ROOT", cast=str, default=os.path.join(BASE_DIR, "uploads/"))

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "db.Student"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
}

SIMPLE_JWT = {
    # Время жизни токена доступа (в данном случае 5 минут)
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    # Время жизни токена обновления (в данном случае 1 день)
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # Указывает, нужно ли обновлять токены обновления при каждом запросе
    "ROTATE_REFRESH_TOKENS": False,
    # Указывает, нужно ли добавлять токен в черный список после его обновления
    "BLACKLIST_AFTER_ROTATION": False,
    # Указывает, нужно ли обновлять время последнего входа пользователя
    "UPDATE_LAST_LOGIN": False,
    # Алгоритм, используемый для подписи токенов (в данном случае HMAC SHA-256)
    "ALGORITHM": "HS256",
    # Ключ для подписи токенов, обычно это SECRET_KEY вашего Django проекта
    "SIGNING_KEY": SECRET_KEY,
    # Ключ для проверки подписи токенов (обычно оставляется пустым)
    "VERIFYING_KEY": "",
    # Аудитория токенов (можно использовать для ограничения использования токена)
    "AUDIENCE": None,
    # Издатель токенов (можно использовать для идентификации источника токена)
    "ISSUER": None,
    # Пользовательский JSON-кодер (можно использовать для изменения способа сериализации)
    "JSON_ENCODER": None,
    # URL для получения JWK (JSON Web Key) для проверки подписи токена (обычно не используется)
    "JWK_URL": None,
    # Допуск по времени для проверки срока действия токена (0 означает отсутствие допуска)
    "LEEWAY": 0,
    # Типы заголовков аутентификации, используемые для передачи токена (в данном случае Bearer)
    "AUTH_HEADER_TYPES": ("Bearer",),
    # Имя заголовка, в котором будет передаваться токен (обычно HTTP_AUTHORIZATION)
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # Поле, представляющее идентификатор пользователя (по умолчанию 'id')
    "USER_ID_FIELD": "id",
    # Поле, в котором будет храниться идентификатор пользователя в токене
    "USER_ID_CLAIM": "user_id",
    # Правило аутентификации пользователя (по умолчанию используется стандартное правило)
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    # Классы токенов аутентификации, которые будут использоваться (в данном случае только AccessToken)
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # Имя поля для указания типа токена (обычно 'token_type')
    "TOKEN_TYPE_CLAIM": "token_type",
    # Класс пользователя токена (по умолчанию TokenUser )
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser ",
    # Уникальный идентификатор токена (JTI - JWT ID)
    "JTI_CLAIM": "jti",
    # Имя поля для указания времени истечения для скользящего токена обновления
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    # Время жизни скользящего токена (в данном случае 5 минут)
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    # Время жизни скользящего токена обновления (в данном случае 1 день)
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # Сериализатор для получения токенов (по умолчанию TokenObtainPairSerializer)
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    # Сериализатор для обновления токенов (по умолчанию TokenRefreshSerializer)
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    # Сериализатор для проверки токенов (по умолчанию TokenVerifySerializer)
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    # Сериализатор для черного списка токенов (по умолчанию TokenBlacklistSerializer)
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    # Сериализатор для получения скользящих токенов (по умолчанию TokenObtainSlidingSerializer)
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    # Сериализатор для обновления скользящих токенов (по умолчанию TokenRefreshSlidingSerializer)
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}


CELERY_BROKER_URL = "pyamqp://rmuser:rmpassword@195.66.114.26:5672//"
CELERY_RESULT_BACKEND = "rpc://"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOSS = True

CELERY_TASK_QUEUES = (
    Queue("queue1", Exchange("my_exchange", type="direct"), routing_key="backup_queue", durable=True),
)

CELERY_TASK_ROUTES = {
    "api.tasks.my_task": {"queue": "queue1"},
}
