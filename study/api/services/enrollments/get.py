from db.models import Enrollment
from django.shortcuts import get_list_or_404
from service_objects.services import Service

from study.utils.logging_config import logger


class GetEnrollmentService(Service):
    def process(self):
        enrollments = get_list_or_404(Enrollment)
        logger.success(
            f"Список о зачислении студентов получен, сервисная часть, колличество записей: {len(enrollments)}"
        )
        return enrollments
