from django.contrib import admin
from .models import Course,Subject
# Register your models here.
@admin.register(Course)
class AdminStudent(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Subject)
class AdminStudent(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')