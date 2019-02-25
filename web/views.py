from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken
from web.core.serializers import  CustomJWTSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


User = get_user_model()
def home(request):
    return render(request, '../templates/site/home.html')

class EmailAsUserLoginView(ObtainJSONWebToken):

    serializer_class = CustomJWTSerializer

