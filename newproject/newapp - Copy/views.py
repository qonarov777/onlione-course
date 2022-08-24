from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, DestroyAPIView,RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import  IsAdminUser
from .models import AboutUs
from .serializers import AboutUsSerializer



class ListCreateAboutUs(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

class DestroyAboutUs(DestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

class RetrieveAboutUs(RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

class UpdateAboutUs(UpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]