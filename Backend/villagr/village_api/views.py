from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from village_api.models import UserProfile, Village, AttendanceLog
from village_api.serializers import UserProfileSerializer, VillageSerializer, AttendanceLogSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceLogViewSet(viewsets.ModelViewSet):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer

#    def perform_create(self, serializer):
#        serializer.save()
#        print(serializer.data)
#        for userid in serializer.data['leaders']:
#            user = UserProfile.objects.get(pk = userid)
#            user.leads_village = serializer.data['id']
#            user.save()