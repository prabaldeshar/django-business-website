from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from helpers.logging_helper import logger

from .models import Project, HomepageSlide
from .serializers import (
    ProjectImageSerializer,
    ProjectSerializer,
    ContactUserSerializer,
    HomepageSlideSerializer,
    
    
)


@api_view(["GET"])
def projects(request):
    logger.info("Getting all projects...")
    # Get query params from request
    logger.info(f"Query params: {request.query_params}")
    project_type = request.query_params.get("type", None)

    if project_type in [Project.PROJECT_TYPE_COMMERCIAL, Project.PROJECT_TYPE_RESIDENTIAL]:
        projects = Project.get_project_by_type(project_type)
    else:
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


@api_view(["GET"])
def get_homepage_slides(request):
    """Retrieve up to three homepage slide images."""
    logger.info("Fetching homepage slides...")
    no_of_slides = request.query_params.get('no_of_slides',None)

    if no_of_slides:
        slides = HomepageSlide.objects.filter(is_visible=True).order_by('-created_at')[:int(no_of_slides)]
    
    else:
        slides = HomepageSlide.objects.filter(is_visible=True).order_by('-created_at')
    
    serialized_slides = HomepageSlideSerializer(slides, many=True).data

    response = {"image_details": serialized_slides}
    logger.info(f"Response: {response}")
    
    return Response(response)


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_homepage_slide(request):
    """Upload a new homepage slide image. Only three images allowed."""
    logger.info("Uploading new homepage slide...")

    # Check if there are already 3 slides
    if HomepageSlide.objects.count() >= 3:
        return Response({"error": "You can only have 3 slide images."}, status=400)

    serializer = HomepageSlideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    logger.error(f"Upload failed: {serializer.errors}")
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_homepage_slide(request, image_id):
    """Delete a homepage slide image."""
    logger.info(f"Deleting homepage slide with ID: {image_id}")

    slide = HomepageSlide.objects.filter(id=image_id).first()

    if not slide:
        logger.error(f"Slide with ID {image_id} does not exist")
        return Response({"error": "Slide not found"}, status=404)

    slide.delete()
    return Response({"message": "Slide deleted successfully"}, status=204)