from rest_framework import serializers

from studentAPI.models import UserType

class UserTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=20)
    class Meta: 
        model = UserType
        fields = ('id', 'name')