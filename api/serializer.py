from rest_framework import serializers

from .models import Classes, Subjects, Users


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=125)


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    user_type = serializers.CharField(max_length=50)

    class Meta:
        model = Users
        fields = ('full_name', 'email', 'user_type')


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    user_type = serializers.CharField(max_length=50)

    class Meta:
        model = Users
        fields = ('full_name', 'email', 'user_type')


class SubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(max_length=50)

    class Meta:
        model = Subjects
        fields = ('subject_id', 'subject_name')


class ClassSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Classes
        fields = ('class_id', 'subject', 'teacher')
