from village_api.models import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    model = UserProfile

    class Meta:
        model = UserProfile
        fields = ['url', 'username']