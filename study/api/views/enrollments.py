from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.enrollment.get import EnrollmentSerializer
from api.services.enrollments.get import GetEnrollmentService


class EnrollmentGetView(APIView):
    def get(self, request, **kwargs):
        enrollments = GetEnrollmentService.execute({})
        serializer = EnrollmentSerializer(enrollments, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)
