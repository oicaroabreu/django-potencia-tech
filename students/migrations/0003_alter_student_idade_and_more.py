# Generated by Django 4.2.6 on 2023-10-30 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_rename_age_student_idade_rename_name_student_nome_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="idade",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(200),
                ],
                verbose_name="Idade",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="nota_do_primeiro_semestre",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="Nota do primeiro semestre",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="nota_do_segundo_semestre",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="Nota do segundo semestre",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="numero_da_sala",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
                verbose_name="Número da sala",
            ),
        ),
    ]