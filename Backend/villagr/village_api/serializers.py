"""
Serializers to convert DB models into JSON
"""
from rest_framework import serializers
from village_api.models import UserProfile, Village, AttendanceLog, Person

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes the UserProfile model
    """
    class Meta:
        model = UserProfile
        fields = ['url', 'username', 'leads_village']

class VillageSerializer(serializers.ModelSerializer):
    """
    Serializes the Village model
    """
    leaders = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=UserProfile.objects.all()
    )

    class Meta:
        model = Village
        fields = ['url', 'description', 'leaders']

    def create(self, validated_data):
        leaders = validated_data.pop('leaders')
        village = Village.objects.create(description=validated_data['description'])
        for user in leaders:
            user.leads_village = village
            user.save()
        return village

class AttendanceLogSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes the Attendance Log model
    """
    #village = serializers.HyperlinkedRelatedField(
    #    many=False,
    #    read_only=True,
    #    allow_null=False,
    #    view_name='villages'
    #)

    class Meta:
        model = AttendanceLog
        fields = ['date', 'person', 'village']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes the Person model
    """
    class Meta:
        model = Person
        fields = ['url', 'phone', 'name', 'discipled_by']
