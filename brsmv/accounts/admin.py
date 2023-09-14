from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

@admin.register(User)
class Blog(UserAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'mobile_no', 'created_at', 'updated_at')
    list_display_links = ('first_name',)
    list_filter = ('first_name', 'middle_name', 'last_name', 'mobile_no', 'created_at', 'updated_at')
    list_per_page = 50
    search_fields = ('first_name', 'mobile_no',)
    readonly_fields = ('created_at', 'updated_at',)
