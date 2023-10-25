import pytest

from ..models import Student
from ..serializers import StudentSerializer


@pytest.mark.django_db
def test_student_serializer_valid(sample_student_data):
    serializer = StudentSerializer(data=sample_student_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_student_serializer_create(sample_student_data):
    serializer = StudentSerializer(data=sample_student_data)
    assert serializer.is_valid()
    serializer.save()
    assert Student.objects.filter(nome="Fernandinho").exists()


@pytest.mark.django_db
def test_student_serializer_update(sample_student_data):
    student = Student.objects.create(**sample_student_data)
    updated_data = {"nome": "Alice", "idade": 24}
    serializer = StudentSerializer(instance=student, data=updated_data, partial=True)
    assert serializer.is_valid()
    serializer.save()
    student.refresh_from_db()
    assert student.nome == "Alice"
    assert student.idade == 24
