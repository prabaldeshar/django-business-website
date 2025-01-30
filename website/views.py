from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from helpers.logging_helper import logger

from .models import Project, ContactUser
from .serializers import (
    ProjectImageSerializer,
    ProjectSerializer,
    ContactUserSerializer,
)


@api_view(["GET"])
def projects(request):
    logger.info("Getting all projects...")
    projects = Project.get_all_projects()
    serilized_projects = ProjectSerializer(projects, many=True).data
    response = {"projects": serilized_projects}
    logger.info(f"Response projects: {response}")
    return Response(response)


@api_view(["GET"])
def project_images(request, project_id):
    logger.info("Getting project images...")
    project = (
        Project.objects.prefetch_related("projectimage_set")
        .filter(id=project_id)
        .first()
    )
    response = {"project": {}, "images": []}
    if not project:
        logger.error(f"Project with the id {project_id} does not exists")
        return Response(response)

    serialized_images = ProjectImageSerializer(
        project.projectimage_set.all(), many=True
    ).data
    serialized_project = ProjectSerializer(project).data

    response = {"project": serialized_project, "images": serialized_images}
    logger.info(f"Response project_images: {response}")

    return Response(response)


@api_view(["POST"])
def contact_user(request):
    logger.info("Input contact data")
    logger.info(request.data)

    serializer = ContactUserSerializer(data=request.data)
    if not serializer.is_valid():
        logger.error(f"Invalid data: {serializer.errors}")
        return Response(serializer.errors, status=400)

    serializer.save()
    logger.info("Contact data saved successfully")

    return Response({"message": "Contact data saved successfully"}, status=200)
