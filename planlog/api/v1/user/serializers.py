from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    full_name = serializers.CharField()
    password = serializers.CharField()
