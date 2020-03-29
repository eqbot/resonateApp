from django.shortcuts import render
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from village_api.models import UserProfile, Village, AttendanceLog, Person
from village_api.serializers import UserProfileSerializer, VillageSerializer, AttendanceLogSerializer, PersonSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class VillageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(detail=True)
    # def attendance(self, request, *args, **kwargs):
    #     village = self.get_object()
    #     attendance_logs = village.attendancelog_set.all()
    #     print(attendance_logs)
    #     if not attendance_logs.exists():
    #         return Response(None)
    #     serializer = AttendanceLogSerializer(attendance_logs, context={'request': request}, many=True)
    #     #print(serializer.data)
    #     return Response(serializer.data)

    # @attendance.mapping.post
    # def add_attendance(self, request, *args, **kwargs):
    #     village = self.get_object()
    #     serializer = AttendanceLogSerializer(request.data)
    #     if serializer.is_valid():
    #         attendance_log = AttendanceLog(village=village, person=serializer.data['person'], date=serializer.data['date'])
    #         attendance_log.save()
    #         return Response({'status': 'attendance added'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceLogViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer