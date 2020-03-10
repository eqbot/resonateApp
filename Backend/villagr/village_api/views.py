from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from village_api.models import UserProfile, Village
from village_api.serializers import UserProfileSerializer, VillageSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]