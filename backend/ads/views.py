from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Ad, Category
from .serializers import AdSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.



class AdViewSet(viewsets.ModelViewSet):
  queryset = Ad.objects.all()
  serializer_class = AdSerializer
  permission_classes = [permissions.AllowAny]
  parser_classes = [MultiPartParser, FormParser]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)