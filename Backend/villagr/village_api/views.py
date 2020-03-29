"""
Defines the behavior of API endpoints
"""

from rest_framework import viewsets, permissions
from rest_framework_extensions.mixins import NestedViewSetMixin
from village_api.models import UserProfile, Village, AttendanceLog, Person
from village_api.serializers import (
    UserProfileSerializer,
    VillageSerializer,
    AttendanceLogSerializer,
    PersonSerializer,
)

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    CRUD operations on user profile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class VillageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    CRUD operations on village
    """
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceLogViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    CRUD operations on attendance log
    """
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    CRUD operations on Person
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    