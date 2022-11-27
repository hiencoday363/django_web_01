from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.views import Token

from .models import UploadImageApi

# the way one
'''
class UploadImageApiSerializer(serializers.Serializer):
    file_name = serializers.CharField(max_length=255)
    myFile = serializers.FileField(max_length=None, allow_empty_file=False)

    def create(self, validated_data):
        return UploadImageApi.objects.create(validated_data)

    def update(self, instance, validated_data):
        pass
'''

# the way two
class UploadImageApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageApi
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password': {
            'required': True,
            'write_only': True
        }}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user


