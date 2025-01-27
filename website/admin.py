from django.contrib import admin
from .models import Project
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'client_name', 'location']
    list_filter = ['project_type']
    search_fields = ['title', 'description', 'client_name', 'location']
