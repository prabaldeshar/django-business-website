from rest_framework import serializers

from website.models import (
    AboutUsPoint,
    HomepageImage,
    Project,
    ProjectImage,
    ContactUser,
    HomepageSlide,
    Service,
    AboutUs,
    ContactInfo,
)


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


class ServiceSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(source="title")
    image = serializers.SerializerMethodField()
    reverse = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ["heading", "description", "image", "reverse"]

    def get_image(self, obj):
        return {
            "src": obj.image.url if obj.image else "",
            "alt": obj.title,
        }

    def get_reverse(self, obj):
        return False


class AboutUsPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPoint
        fields = ["title", "description"]


class AboutUsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    points = AboutUsPointSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ["heading", "description", "image", "points"]

    def get_image(self, obj):
        return {
            "src": obj.image.url if obj.image else "",
            "alt": obj.heading,
        }


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class HomepageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageImage
        fields = ["id", "section", "image", "title"]
