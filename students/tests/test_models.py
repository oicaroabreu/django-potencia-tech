import pytest

from ..models import Student


@pytest.mark.django_db
def test_student_attributes(student_instance):
    assert student_instance.nome == "Fernandinho"
    assert student_instance.idade == 25
    assert student_instance.nota_do_primeiro_semestre == 9.0
    assert student_instance.nota_do_segundo_semestre == 8.5
    assert student_instance.nome_do_professor == "Prossora Bete"
    assert student_instance.numero_da_sala == 10


@pytest.mark.django_db
def test_student_verbose_name():
    nome = Student._meta.get_field("nome")
    idade = Student._meta.get_field("idade")
    nota_do_primeiro_semestre = Student._meta.get_field("nota_do_primeiro_semestre")
    nota_do_segundo_semestre = Student._meta.get_field("nota_do_segundo_semestre")
    nome_do_professor = Student._meta.get_field("nome_do_professor")
    numero_da_sala = Student._meta.get_field("numero_da_sala")

    assert nome.verbose_name == "Nome"
    assert idade.verbose_name == "Idade"
    assert nota_do_primeiro_semestre.verbose_name == "Nota do primeiro semestre"
    assert nota_do_segundo_semestre.verbose_name == "Nota do segundo semestre"
    assert nome_do_professor.verbose_name == "Nome do professor"
    assert numero_da_sala.verbose_name == "Número da sala"
