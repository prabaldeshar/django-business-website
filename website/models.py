from django.db import models
from datetime import date
import django.core.validators
from django.core.exceptions import ValidationError


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
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AboutUs(BaseModel):
    heading = models.CharField(max_length=200)
    description = models.TextField()

    def clean(self):
        # Prevent multiple instances
        if not self.pk and AboutUs.objects.exists():
            raise ValidationError(
                "AboutUS already exists. You can only edit the existing entry."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        # Ensure only one instance exists
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError("Only one AboutUs instance is allowed.")
        super().save(*args, **kwargs)

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


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, help_text="Contact phone number")
    email = models.EmailField(help_text="Contact email address", null=True, blank=True)
    address = models.CharField(max_length=200, help_text="Current Address")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook page URL")
    instagram = models.URLField(
        blank=True, null=True, help_text="Instagram profile URL"
    )

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def clean(self):
        # Prevent multiple instances
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError(
                "Contact information already exists. You can only edit the existing entry."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        # Ensure only one instance exists
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError("Only one ContactInfo instance is allowed.")
        super().save(*args, **kwargs)

    @classmethod
    def get_contact_info(cls):
        """Get the single contact info instance, create if doesn't exist"""
        contact_info, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                "phone": "",
                "email": "",
                "facebook": "",
                "instagram": "",
            },
        )
        return contact_info

    def __str__(self):
        return f"Contact Info - {self.email}"


class HomepageImage(BaseModel):
    SECTION_CHOICES = [
        ("about_us", "About Us"),
        ("services", "Services"),
        ("projects", "Projects"),
    ]

    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    image = models.ImageField(upload_to="homepage/")
    title = models.CharField(max_length=255, blank=True, null=True)

    def clean(self):
        # Restrict number of images per section
        max_images = {
            "about_us": 1,
            "services": 1,
            "projects": 3,
        }
        current_count = (
            HomepageImage.objects.filter(section=self.section)
            .exclude(pk=self.pk)
            .count()
        )
        if current_count >= max_images.get(self.section, 0):
            raise ValidationError(
                f"Only {max_images[self.section]} image(s) allowed for {self.section.replace('_', ' ').title()} section."
            )

    def save(self, *args, **kwargs):
        self.full_clean()  # Call clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.section.title()} - {self.title or self.image.name}"
