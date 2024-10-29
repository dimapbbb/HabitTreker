from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'last_name', 'first_name')

