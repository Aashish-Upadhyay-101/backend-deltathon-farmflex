from rest_framework import serializers
from .models import Profile
from apps.common.serializers import UserModelSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Profile 
        exclude = ["pkid"]


class ProfileUpdateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["phone_number", "country", "zip_code", "city", "profile_type"]
