from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline

from .models import Project, ProjectImage, ContactUser, HomepageSlide


class ProjectImageInline(TabularInline):
    model = ProjectImage
    readonly_fields = ("image_preview",)
    exclude = ("deleted_at", "is_deleted", "description")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" style="max-height: 50px; max-width: 200px; cursor: pointer;"/>'
                "</a>",
                obj.image.url,
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["title", "client_name", "location", "image_preview"]
    list_filter = ["project_type"]
    search_fields = ["title", "description", "client_name", "location"]
    exclude = ("deleted_at", "is_deleted")
    inlines = [
        ProjectImageInline,
    ]

    def image_preview(self, obj: Project):
        if obj.cover_image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" style="max-height: 50px; max-width: 200px; cursor: pointer;"/>'
                "</a>",
                obj.cover_image.url,  # Full-size image link
                obj.cover_image.url,  # Thumbnail souxrce
            )
        return "No Image"

    image_preview.short_description = "Cover Image"


@admin.register(ContactUser)
class ContactUserAmdin(ModelAdmin):
    list_display = ["name", "email", "phone", "subject", "message", "created_at"]
    exclude = ("deleted_at", "is_deleted")


@admin.register(HomepageSlide)
class HomepageSlideAdmin(ModelAdmin):
    list_display = (
        "title",
        "image_preview",
        "uploaded_at",
    )  # Columns in the admin panel
    ordering = ["-uploaded_at"]  # Order by latest uploaded

    def image_preview(self, obj: HomepageSlide):
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" style="max-height: 50px; max-width: 200px; cursor: pointer;"/>'
                "</a>",
                obj.image.url,  # Full-size image link
                obj.image.url,  # Thumbnail souxrce
            )
        return "No Image"

    image_preview.short_description = "Cover Image"
