from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cerberus import Validator
from .models import User
# Create your views here.
class UserApi(APIView):
    def post(self,request):
        validator = Validator({
            "name":{"required":True,"type":"string"},
            "doc":{"required":True,"type":"string"},
            "profile":{"required":True,"type":"string"},
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_filtering_params",
                "detailed": "Parámetros de búsqueda inválidos",
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(request.data).pk
        return Response(
            {
                "pk":user
            },status=status.HTTP_201_CREATED
        )
    def get(self,request):
        user = User.objects.all()

        return Response({
            "data":user.values()
        },status=status.HTTP_200_OK)
    
        