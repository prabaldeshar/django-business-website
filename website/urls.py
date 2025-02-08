from . import views
from django.urls import path, include
from .views import (
    projects,
    project_images,
    contact_user,
    get_homepage_slides,
    upload_homepage_slide,
    delete_homepage_slide,
)


urlpatterns = [
    path("project/list/", projects, name="Project List"),
    path("project/images/<str:project_id>/", project_images, name="Project Images"),
    path("contact/user/", contact_user, name="Contact User"),
    path("homepage-slides/", get_homepage_slides, name="homepage-slides"),
    path(
        "homepage-slides/upload/", upload_homepage_slide, name="upload-homepage-slide"
    ),
    path(
        "homepage-slides/<int:image_id>/delete/",
        delete_homepage_slide,
        name="delete-homepage-slide",
    ),
]
