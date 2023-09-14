from django.contrib import admin
from .models import Student, StudentDocument, Course, Subject, StudentSubject


# Register your models here.

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('student_id', 'aadhar', 'father_name', 'enroll_year', 'enroll_end_year',)
    list_display_links = ('student_id', 'aadhar', 'father_name', 'enroll_year', 'enroll_end_year',)
    list_per_page = 50
    readonly_fields = ('enroll_year', 'enroll_end_year', 'created_at', 'updated_at')


@admin.register(StudentDocument)
class AdminStudent(admin.ModelAdmin):
    list_display = ('student_id',)
    list_display_links = ('student_id',)
    list_per_page = 50
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StudentSubject)
class AdminStudent(admin.ModelAdmin):
    list_display = ('student_id',)
    list_display_links = ('student_id',)
    list_per_page = 50
    readonly_fields = ('created_at', 'updated_at')
