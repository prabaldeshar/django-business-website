from . import views
from django.urls import path, include
from .views import (
    get_about_us,
    homepage_images,
    projects,
    project_images,
    contact_user,
    get_homepage_slides,
    upload_homepage_slide,
    delete_homepage_slide,
    get_services,
    get_contact_information,
)


urlpatterns = [
    path("project/list/", projects, name="Project List"),
    path("project/images/<str:project_id>/", project_images, name="Project Images"),
    path("contact/user/", contact_user, name="Contact User"),
    path("homepage-slides/", get_homepage_slides, name="homepage-slides"),
    path("services/", get_services, name="services"),
    path("about-us/", get_about_us, name="about-us"),
    path("homepage-images/", homepage_images, name="homepage-images"),
    path("contact-info/", get_contact_information, name="contact-info"),
    path(
        "homepage-slides/upload/", upload_homepage_slide, name="upload-homepage-slide"
    ),
    path(
        "homepage-slides/<int:image_id>/delete/",
        delete_homepage_slide,
        name="delete-homepage-slide",
    ),
]
