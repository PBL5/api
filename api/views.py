from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Classes, Details_Student_Attend_Class, Users
from .serializer import ClassSerializer, LoginSerializer, StudentSerializer, UserSerializer


class StudentAPIView(generics.GenericAPIView):
    serializer_class = StudentSerializer
    class_id_param = openapi.Parameter('class_id',
                                       in_=openapi.IN_QUERY,
                                       type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[class_id_param])
    def get(self, request):
        class_id = request.query_params['class_id']

        student = Details_Student_Attend_Class.objects.filter(course__pk=class_id).values_list()
        print(student[0][1])
        print(student)
        return Response()


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
