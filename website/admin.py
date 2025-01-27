from django.contrib import admin
from .models import Project, ProjectImage
# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    exclude = ('deleted_at', 'is_deleted')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'client_name', 'location']
    list_filter = ['project_type']
    search_fields = ['title', 'description', 'client_name', 'location']
    exclude = ('deleted_at', 'is_deleted')
    inlines =[ProjectImageInline, ]
