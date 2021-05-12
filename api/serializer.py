from rest_framework import serializers

from .models import User_Types, Users, Subject, DateClass, Class, DetailStudentAttendClass, StudentAttending


class UserTypeSerializer(serializers.ModelSerializer):
    user_type_id = serializers.IntegerField()
    user_type_name = serializers.CharField(max_length=20)

    class Meta:
        model = User_Types
        fields = ('user_type_id', 'user_type_name')


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)
    user_type = serializers.CharField(max_length=50)

    class Meta:
        model = Users
        fields = ('full_name', 'email', 'user_type', 'password')


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    class Meta:
        model = Users
        fields = ('email', 'password')


class SubjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Subject
        fields = ('id', 'name')


class ClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    subject = serializers.UUIDField()
    teacher = serializers.IntegerField()

    class Meta:
        model = Class
        fields = ('name', 'subject', 'teacher')


class DateClassSerializer(serializers.ModelSerializer):
    Date = serializers.UUIDField()
    Class = serializers.UUIDField()

    class Meta:
        model = DateClass
        fields = ('__all__')

# class DetailStudentAttendClassSerializer(serializers.ModelSerializer):
# student = serializers.IntegerField()
# Class = serializers.UUIDField()
# class Meta:
# model = DetailStudentAttendClass
# fields = ('student', 'Class')

# class StudentAttendingSerializer(serializers.ModelSerializer):
# isAttending = serializers.BooleanField()
# dateClass = serializers.UUIDField()
# student = serializers.IntegerField()
# class Meta:
# model = Class
# fields = ('isAttending', 'dateClass', 'student')
