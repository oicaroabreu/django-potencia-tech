from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
        "first_semester_grade",
        "second_semester_grade",
        "professor_name",
        "room_number",
    )
    list_filter = ("age", "professor_name", "room_number")
    search_fields = ("name", "professor_name", "room_number")
    list_per_page = 25
