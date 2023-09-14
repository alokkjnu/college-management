from django.contrib import admin
from .models import College


# Register your models here.

@admin.register(College)
class College(admin.ModelAdmin):
    list_display = ('college_id', 'college_name',)
    list_filter = ('college_id', 'college_name',)
    list_display_link = ('college_name',)
    list_per_page = 50
    readonly_fields = ('college_id', 'college_name',)
