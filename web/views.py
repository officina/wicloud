from django.shortcuts import render
from rest_framework_jwt.views import ObtainJSONWebToken
from web.core.serializers import  CustomJWTSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
def  home(request):
    return render(request, '../templates/site/home.html')

class EmailAsUserLoginView(ObtainJSONWebToken):

    serializer_class = CustomJWTSerializer
