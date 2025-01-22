from . import views
from django.urls import path, include
from .views import projects, project_images

urlpatterns = [
    path("", views.home),
    path("project/list/", projects, name="Project List"),
    path("project/images/<str:project_id>/", project_images, name="Project Images")
]
