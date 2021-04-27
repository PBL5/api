from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserType
from .serializer import UserTypeSerializer

@api_view(['GET'])
def UserTypesView(request):
    return JsonResponse("API BASE POINT", safe=False)

@api_view(['GET'])
def userTypeList(request):
    userTypes = UserType.objects.all()
    serializer = UserTypeSerializer(userTypes, many=True)
    return JsonResponse(serializer.data, safe=False)