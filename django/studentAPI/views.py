from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import UserType
from .serializer import UserTypeSerializer
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserTypesAPIView(generics.GenericAPIView):
    serializer_class = UserTypeSerializer
    throttle_scope = "userTypes_app"
    get_byID_param = openapi.Parameter('id', in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)

    def get_queryset(self):
        userTypes = UserType.objects.all()
        return userTypes

    @swagger_auto_schema(manual_parameters=[get_byID_param])
    def get(self, request):
        id = request.query_params["id"]
        userType = UserType.objects.get(id=id)
        serializer = UserTypeSerializer(userType)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        userType_data = request.data

        new_userType = UserType.objects.create(id=userType_data["id"], name=userType_data["name"])

        new_userType.save()

        serializer = UserTypeSerializer(new_userType)

        return Response(serializer.data)
