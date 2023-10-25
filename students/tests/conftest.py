import pytest

from ..models import Student


@pytest.fixture
def student_instance():
    return Student.objects.create(
        nome="Fernandinho",
        idade=25,
        nota_do_primeiro_semestre=9.0,
        nota_do_segundo_semestre=8.5,
        nome_do_professor="Prossora Bete",
        numero_da_sala=10,
    )


@pytest.fixture
def sample_student_data():
    return {
        "nome": "Fernandinho",
        "idade": 25,
        "nota_do_primeiro_semestre": 9.0,
        "nota_do_segundo_semestre": 8.5,
        "nome_do_professor": "Prossora Bete",
        "numero_da_sala": 10,
    }
