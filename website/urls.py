from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home),
    path('contact',views.contact,name='contact')
    
]
