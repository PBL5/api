from rest_framework import serializers

from studentAPI.models import UserType

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserType
        fields = ('id', 'name')