from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from village_api.models import UserProfile
from village_api.serializers import UserProfileSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

