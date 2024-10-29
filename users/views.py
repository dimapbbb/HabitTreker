from django.contrib.auth.hashers import make_password
from rest_framework import generics

from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.password = make_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()