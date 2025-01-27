from rest_framework import serializers

from website.models import Project, ProjectImage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'client_name', 'location', 'project_type', 'completed_date', 'cover_image']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'description',]
