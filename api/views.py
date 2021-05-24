from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from .models import Classes, Users
from .serializer import (ClassSerializer, LoginSerializer,
                         StudentFilterSerializer, UserSerializer)


class StudentAPIView(generics.GenericAPIView):
    @swagger_auto_schema(request_body=StudentFilterSerializer)
    def post(self, request):
        class_id = request.data['class_id']

        students = Users.objects.filter(
            details_student_attend_class__course__pk=class_id)

        if 'filter_options' in request.data:
            filter_options = request.data['filter_options']
            if 'gender' in filter_options:
                students = students.filter(gender=filter_options['gender'])

            if 'full_name' in filter_options:
                students = students.filter(
                    full_name=filter_options['full_name'])

            if 'email' in filter_options:
                students = students.filter(email=filter_options['email'])

            if 'user_id' in filter_options:
                students = students.filter(user_id=filter_options['user_id'])

            if 'birthday' in filter_options:
                students = students.filter(birthday=filter_options['birthday'])

        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)


class ClassAPIView(generics.GenericAPIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LoginAPIView(generics.GenericAPIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        try:
            user = Users.objects.get(email=email)

            if user.password == password:
                serializer = UserSerializer(user)
                return Response(serializer.data)
            return HttpResponse('Password incorrect.', status=401)
        except ObjectDoesNotExist:
            return HttpResponse("User doesn't exist", status=401)
