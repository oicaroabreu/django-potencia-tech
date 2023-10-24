from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Nome")
    age = models.IntegerField(verbose_name="Idade")
    first_semester_grade = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Nota do primeiro semestre"
    )
    second_semester_grade = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Nota do segundo semestre"
    )
    professor_name = models.CharField(max_length=100, verbose_name="Nome do professor")
    room_number = models.CharField(max_length=10, verbose_name="Número da sala")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"
