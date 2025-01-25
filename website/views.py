from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


SAMPLE_PROJECTS =  [
        {
            "id": "project_1",
            "title": "Modern Living Room",
            "description": "A sleek and modern living room design with a focus on minimalism.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.16.18+PM.jpeg"
        },
        {
            "id": "project_2",
            "title": "Elegant Office Space",
            "description": "An office space that combines functionality with elegance.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.29.16+PM+(2).jpeg"
        },
        {
            "id": "project_3",
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg"
        },
         {
            "id": "project_4",
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg"
        },
        {
            "id": "project_5",
            "title": "Elegant Office Space",
            "description": "An office space that combines functionality with elegance.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.29.16+PM+(2).jpeg"
        },
        {
            "id": "project_6",
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg"
        },
         {
            "id": "project_7",
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg"
        },
         {
            "id": "project_8",
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg"
        },
         {
            "id": "project_9",
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg"
        },
        {
            "id": "project_10",
            "title": "Elegant Office Space",
            "description": "An office space that combines functionality with elegance.",
            "image": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.29.16+PM+(2).jpeg"
        }
    ]

SAMPLE_PROJECT_IMAGES = {
    "project_1": {
        "images": [
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.16.18+PM.jpeg", "alt": "Img"},
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.16.19+PM+(1).jpeg", "alt": "Img"},
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.16.19+PM+(2).jpeg", "alt": "Img"}
        ]

    },
    "project_2": {
        "images": [
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.29.16+PM+(2).jpeg", "alt": "Img"},
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.29.16+PM+(1).jpeg", "alt": "Img"},
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.29.16+PM+(2).jpeg", "alt": "Img"}
        ]

    },
    "project_3": {
        "images": [
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg", "alt": "Img"},
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(1).jpeg", "alt": "Img"},
            {"src": "https://ideal-interior-nepal.s3.ap-south-1.amazonaws.com/sample-project/WhatsApp+Image+2025-01-20+at+7.33.16+PM+(2).jpeg", "alt": "Img"}
        ]

    }
}

hero_image_path = "static/images/design-1.png"
# Create your views here.
def home(request):
    return render(request, "website/home.html", context={"projects": SAMPLE_PROJECTS, "hero_image_path": hero_image_path})


@api_view(['GET'])
def projects(request):
    response = {"projects": SAMPLE_PROJECTS}
    return Response(response)


@api_view(['GET'])
def project_images(request, project_id):
    images = SAMPLE_PROJECT_IMAGES.get(project_id, {}).get("images", [])
    response = {"project_id": project_id, "images": images}
    
    return Response(response)
