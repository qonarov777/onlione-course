from .views import ListCreateAboutUs, DestroyAboutUs,RetrieveAboutUs, UpdateAboutUs
from django.urls import path



urlpatterns = [
    path('',ListCreateAboutUs.as_view()),
    path('delete/<int:pk>', DestroyAboutUs.as_view()),
    path('get/<int:pk>', RetrieveAboutUs.as_view()),
    path('put/<int:pk>', UpdateAboutUs.as_view()),
]
