from . import views
from django.urls import path, include
from .views import projects, project_images, contact_user

urlpatterns = [
    path("project/list/", projects, name="Project List"),
    path("project/images/<str:project_id>/", project_images, name="Project Images"),
    path("contact/user/", contact_user, name="Contact User")
]
