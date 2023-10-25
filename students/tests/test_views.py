from decimal import Decimal
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Student
from ..serializers import StudentSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_student_list(api_client, sample_student_data):
    url = reverse("student-list")
    
    response = api_client.post(url, sample_student_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    assert Student.objects.filter(nome="Fernandinho").exists()

@pytest.mark.django_db
def test_student_detail_get(api_client, sample_student_data):
    student = Student.objects.create(**sample_student_data)
    url = reverse("student-detail", args=[student.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert response.data == StudentSerializer(student).data

@pytest.mark.django_db
def test_student_detail_patch(api_client, sample_student_data):
    student = Student.objects.create(**sample_student_data)
    url = reverse("student-detail", args=[student.id])

    updated_data = {"nome": "Rafaela", "idade": 29}
    response = api_client.patch(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK

    student.refresh_from_db()
    assert student.nome == "Rafaela"
    assert student.idade == 29

@pytest.mark.django_db
def test_student_detail_put(api_client, sample_student_data):
    student = Student.objects.create(**sample_student_data)
    url = reverse("student-detail", args=[student.id])

    updated_data = {
        "nome": "Alice",
        "idade": 23,
        "nota_do_primeiro_semestre": 9.2,
        "nota_do_segundo_semestre": 8.9,
        "nome_do_professor": "Simbalena",
        "numero_da_sala": 13,
    }
    response = api_client.put(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK

    student.refresh_from_db()
    assert student.nome == "Alice"
    assert student.idade == 23
    assert student.nota_do_primeiro_semestre == Decimal('9.20')
    assert student.nota_do_segundo_semestre == Decimal('8.90')
    assert student.nome_do_professor == "Simbalena"
    assert student.numero_da_sala == 13

@pytest.mark.django_db
def test_student_detail_delete(api_client, sample_student_data):
    student = Student.objects.create(**sample_student_data)
    url = reverse("student-detail", args=[student.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Student.objects.filter(id=student.id).exists()
