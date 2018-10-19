from rest_framework_jwt.serializers import JSONWebTokenSerializer

from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User = get_user_model()

class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("email")).first() or User.objects.filter(username=attrs.get("email")).first()
        if user_obj is not None:
            credentials = {
                'username':user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)


class CustomTokenResponseSerializer(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': CustomTokenResponseSerializer(user, context={'request':request}).data
    }
