from rest_framework import serializers
from planlog.models.user import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    full_name = serializers.CharField()
    password = serializers.CharField()


class LoggedInUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'full_name',
            'avatar',
            'access_token',
            'refresh_token',
        ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'full_name',
            'avatar',
            'access_token',
            'refresh_token',
        ]
