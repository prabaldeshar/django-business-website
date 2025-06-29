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
    PROJECT_TYPE_RESIDENTIAL = "Residential"
    PROJECT_TYPE_COMMERCIAL = "Commercial"

    project_type_choices = [
        (PROJECT_TYPE_RESIDENTIAL,) * 2,
        (PROJECT_TYPE_COMMERCIAL,) * 2,
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.FileField(
        null=True,
        blank=True,
        upload_to="projects/images/",
        validators=[
            django.core.validators.FileExtensionValidator(
                allowed_extensions=["jpeg", "jpg", "png"]
            )
        ],
    )
    project_type = models.CharField(
        max_length=20, choices=project_type_choices, default=PROJECT_TYPE_COMMERCIAL
    )
    completed_date = models.DateField(default=date.today, null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_project_by_id(cls, project_id):
        try:
            return Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return None

    @classmethod
    def get_all_projects(cls):
        return Project.objects.all().order_by("-created_at")

    @classmethod
    def get_project_by_type(cls, project_type):
        return Project.objects.filter(project_type=project_type).order_by("-created_at")


class ProjectImage(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.FileField(
        null=True,
        blank=True,
        upload_to="projects/images/",
        validators=[
            django.core.validators.FileExtensionValidator(
                allowed_extensions=["jpeg", "jpg", "png"]
            )
        ],
    )
    description = models.TextField(null=True, blank=True)


class ContactUser(BaseModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"


class HomepageSlide(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="homepage_slides/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Service(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title


class AboutUs(BaseModel):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="points/")

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class AboutUsPoint(models.Model):
    about_us = models.ForeignKey(
        AboutUs, related_name="points", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
