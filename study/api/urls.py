from django.urls import path

from api.views.enrollments import EnrollmentGetView
from api.views.students import StudentGetView, StudentView

urlpatterns = [

    path('students/<int:id>/', StudentView.as_view(), name='student-detail'),
    path('students/', StudentGetView.as_view(), name='student-adults'),
    path('enrollment/', EnrollmentGetView.as_view(), name='enrollments'),
]
