FROM python:3.10.11-slim

WORKDIR /django_test_pj

RUN apt-get update && apt-get install -y netcat
# Устанавливаем uv (если нужно)
RUN pip install uv

# Копируем файлы зависимостей
COPY pyproject.toml uv.lock* ./


# Устанавливаем зависимости через uv
RUN uv sync

#ENV PYTHONPATH=/django_test_pj/study
ENV PYTHONPATH=/django_test_pj

# Копируем приложение
COPY study/ study/


ENV DJANGO_SETTINGS_MODULE=study.conf.settings
EXPOSE 8000

#CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "study.conf.wsgi:application"]


