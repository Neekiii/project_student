from django.contrib import admin
from app_students.models import StudentModel
# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","contact","course")
    search_fields=("first_name","contact")
    list_filter=("first_name",)
admin.site.register(StudentModel,StudentModelAdmin)