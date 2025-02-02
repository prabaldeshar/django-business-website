from rest_framework import serializers

from website.models import Project, ProjectImage, ContactUser, HomepageSlide


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "client_name",
            "location",
            "project_type",
            "description",
            "completed_date",
            "cover_image",
        ]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = [
            "id",
            "image",
            "description",
        ]


class ContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUser
        fields = "__all__"

    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)


class HomepageSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageSlide
        fields = ["id", "title", "image", "uploaded_at"]
