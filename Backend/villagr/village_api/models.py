from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Person(models.Model):
    """
    Information on a village attendee
    """
    phone = PhoneField(primary_key=True)
    name = models.CharField(max_length=128)
    discipled_by = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)

class Village(models.Model):
    """
    A village
    """
    description = models.CharField(max_length=128)

class UserProfile(AbstractUser):
    """
    Application user data
    """
    leads_village = models.ForeignKey(
        Village,
        on_delete=models.SET_NULL,
        null=True,
        related_name='leaders'
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class AttendanceLog(models.Model):
    """
    Village attendance log
    """
    WEEKLYMEETING = 'WM'
    OTHER = 'OT'
    MEETING_TYPES = [
        (WEEKLYMEETING, 'Weekly Meeting'),
        (OTHER, "Other")
    ]
    date = models.DateField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    