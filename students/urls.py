from django.urls import path

from .views import StudentDetail, StudentList

urlpatterns = [
    path("v1/alunos/", StudentList.as_view(), name="student-list"),
    path("v1/alunos/<int:pk>/", StudentDetail.as_view(), name="student-detail"),
]
