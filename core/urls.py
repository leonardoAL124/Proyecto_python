from django.urls import path
from core import views as core_views

urlpatterns = [
    path('about/', core_views.about, name="about"),
    path('contact/', core_views.contact, name="contact"),
]