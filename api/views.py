from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Classes, Users
from .serializer import ClassSerializer, StudentSerializer, UserSerializer


class StudentAPIView(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get(self, request):
        students = Users.objects.filter(user_type=1)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class ClassAPIView(generics.GenericAPIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LoginAPIView(generics.GenericAPIView):
    #  serializer_class = UserSerializer
    email_param = openapi.Parameter('email',
                                    in_=openapi.IN_QUERY,
                                    type=openapi.TYPE_STRING)
    password_param = openapi.Parameter('password',
                                       in_=openapi.IN_QUERY,
                                       type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[email_param, password_param])
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
