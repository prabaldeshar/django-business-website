from django.shortcuts import render


SAMPLE_PROJECTS =  [
        {
            "id": 1,
            "title": "Modern Living Room",
            "description": "A sleek and modern living room design with a focus on minimalism.",
            "image": "static/images/design-1.png"
        },
        {
            "id": 2,
            "title": "Elegant Office Space",
            "description": "An office space that combines functionality with elegance.",
            "image": "static/images/design-3.jpg"
        },
        {
            "id": 3,
            "title": "Cozy Bedroom Design",
            "description": "A warm and inviting bedroom for ultimate relaxation.",
            "image": "static/images/design-4.jpg"
        }
    ]

hero_image_path = "static/images/design-1.png"
# Create your views here.
def home(request):
    return render(request, "website/home.html", context={"projects": SAMPLE_PROJECTS, "hero_image_path": hero_image_path}) 