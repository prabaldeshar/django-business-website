from django.db import models
from datetime import date
import django.core.validators

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Project(BaseModel):
    PROJECT_TYPE_RESIDENTIAL = "RESIDENTIAL"
    PROJECT_TYPE_COMMERCIAL = "COMMERCIAL"

    project_type_choices = [
        (PROJECT_TYPE_RESIDENTIAL, ) * 2,
        (PROJECT_TYPE_COMMERCIAL, ) * 2
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.FileField(null=True, blank=True, upload_to='projects/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'pdf'])])
    project_type = models.CharField(max_length=20, choices=project_type_choices, default=PROJECT_TYPE_COMMERCIAL)
    completed_date = models.DateField(default=date.today, null=True, blank=True)


class ProjectImage(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    image = models.FileField(null=True, blank=True, upload_to='projects/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'pdf'])])
    description = models.TextField(null=True, blank=True)
