from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ProjectImageSerializer

@api_view(['GET'])
def projects(request):
    projects = Project.objects.all()
    serilized_projects = ProjectSerializer(projects, many=True).data
    response = {"projects": serilized_projects}
    return Response(response)


@api_view(['GET'])
def project_images(request, project_id):
    project = (
        Project.objects.prefetch_related(
            'projectimage_set'  # Prefetch related images to avoid additional queries
        )
        .filter(id=project_id)
        .first()
    )
    response = {"project": {}, "images": []}
    if not project:
        return Response(response)
        
    serialized_images = ProjectImageSerializer(project.projectimage_set.all(), many=True).data
    serialized_project = ProjectSerializer(project).data
    response = {"project": serialized_project, "images": serialized_images}
    
    return Response(response)
