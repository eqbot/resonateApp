from village_api.models import UserProfile, Village
from rest_framework import serializers

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['url', 'username']

class VillageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Village
        fields = ['description']