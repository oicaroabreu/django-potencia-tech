from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    idade = models.IntegerField(
        verbose_name="Idade", validators=[MinValueValidator(0), MaxValueValidator(200)]
    )
    nota_do_primeiro_semestre = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Nota do primeiro semestre",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    nota_do_segundo_semestre = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Nota do segundo semestre",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    nome_do_professor = models.CharField(
        max_length=100, verbose_name="Nome do professor"
    )
    numero_da_sala = models.IntegerField(
        verbose_name="Número da sala",
        validators=[MinValueValidator(0), MaxValueValidator(10000)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"
