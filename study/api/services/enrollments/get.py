from db.models import Enrollment
from django.shortcuts import get_list_or_404
from service_objects.services import Service


class GetEnrollmentService(Service):

    def process(self):
        obj = get_list_or_404(Enrollment)
        return obj
