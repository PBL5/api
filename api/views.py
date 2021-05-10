from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import UserType, User, Subject, DateClass, Class, DetailStudentAttendClass, StudentAttending
from .serializer import UserTypeSerializer, UserSerializer, SubjectSerializer, ClassSerializer, DateClassSerializer
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import uuid

class UserTypesAPIView(generics.GenericAPIView):
    serializer_class = UserTypeSerializer
    throttle_scope = "userTypes_app"

    def get(self, request):
        userTypes = UserType.objects.all()
        serializer = UserTypeSerializer(userTypes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        userType_data = request.data

        new_userType = UserType.objects.create(id=userType_data["id"], name=userType_data["name"])

        new_userType.save()

        serializer = UserTypeSerializer(new_userType)

        return Response(serializer.data)

class UserAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    throttle_scope = "users_app"

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserGetAPIView(generics.GenericAPIView):
    get_byID_param = openapi.Parameter('id', in_=openapi.IN_QUERY,type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(manual_parameters=[get_byID_param])
    def get(self, request):
        id = request.query_params["id"]
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LoginAPIView(generics.GenericAPIView):
    email_param = openapi.Parameter('email', in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    password_param = openapi.Parameter('password', in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[email_param, password_param])
    def post(self, request, *args, **kwargs):

        email = request.query_params["email"]
        password = request.query_params["password"]
        try:
            user = User.objects.get(email=email)

            if user.password == password:
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return HttpResponse('Password incorrect.', status=404)
        except ObjectDoesNotExist:
                return HttpResponse("User doesn't exist", status=404)

class SignUpAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    throttle_scope = "users_app"
    def post(self, request, *args, **kwargs):
        user_data = request.data
        user_type = UserType.objects.get(name=user_data["usertype"])
        id = User.objects.latest('id').id + 1
        new_user = User.objects.create(id=id, name=user_data["name"], email=user_data["email"], usertype=user_type, password=user_data["password"])
        new_user.save()

        serializer = UserSerializer(new_user)
        return Response(serializer.data)

class SubjectsAPIView(generics.GenericAPIView):
    throttle_scope = "subjects_app"
    name_param = openapi.Parameter('name', in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[name_param])
    def post(self, request, *args, **kwargs):
        name = request.query_params["name"]
        id = uuid.uuid4()
        new_subject = Subject.objects.create(id=id, name=name)
        new_subject.save()
        serializer = SubjectSerializer(new_subject)
        return Response(serializer.data)

class ClasssAPIView(generics.GenericAPIView):
    serializer_class = ClassSerializer
    throttle_scope = "classes_app"

    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        class_data = request.data
        id = Class.objects.latest('id').id + 1
        subject = Subject.objects.get(id=class_data["subject"])
        teacher = User.objects.get(id=class_data["teacher"])
        new_class = Class.objects.create(id=id, name=class_data["name"], subject = subject, teacher = teacher)
        new_class.save()
        serializer = ClassSerializer(new_class)
        return Response(serializer.data)


        
class DateClassAPIView(generics.GenericAPIView):
    serializer_class = DateClassSerializer
    throttle_scope = "dateClasses_app"

    def get(self, request):
        dateClasses = DateClass.objects.all()
        serializer = DateClassSerializer(dateClasses, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        dateClass_data = request.data
        id = DateClass.objects.latest('id').id + 1
        date = Date.objects.get(id=class_data["Date"])
        Class = Class.objects.get(id=class_data["Class"])
        new_dateClass = Class.objects.create(id=id, date=date, Class = Class)
        new_dateClass.save()
        serializer = ClassSerializer(new_dateClass)
        return Response(serializer.data)



