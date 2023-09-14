from django.contrib import admin
from .models import Blog


# Register your models here.

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('blog_title', "user", "college", 'created_at', 'updated_at',)
    list_display_links = ('blog_title',)
    list_filter = ('blog_title', "user", "college", 'created_at', 'updated_at',)
    list_per_page = 50
    readonly_fields = ('created_at', 'updated_at',)
