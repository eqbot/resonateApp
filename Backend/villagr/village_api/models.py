from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    phone = PhoneField(primary_key=True)
    name = models.CharField(max_length=128)
    discipled_by = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)

class Village(models.Model):
    description = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leads_village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)

class AttendanceLog(models.Model):
    WEEKLYMEETING = 'WM'
    OTHER = 'OT'
    MEETING_TYPES = [
        (WEEKLYMEETING, 'Weekly Meeting'),
        (OTHER, "Other")
    ]
    date = models.DateField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    