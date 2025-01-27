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
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.FileField(null=True, blank=True, upload_to='projects/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'pdf'])])
    completed_date = models.DateField(default=date.today, null=True, blank=True)
