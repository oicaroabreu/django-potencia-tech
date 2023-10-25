from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "idade",
        "nota_do_primeiro_semestre",
        "nota_do_segundo_semestre",
        "nome_do_professor",
        "numero_da_sala",
    )
    list_filter = ("idade", "nome_do_professor", "numero_da_sala")
    search_fields = ("nome", "nome_do_professor", "numero_da_sala")
    list_per_page = 25
