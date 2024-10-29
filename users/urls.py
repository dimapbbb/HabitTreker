from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', UserListAPIView.as_view(), name='users'),
    path('update_user/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user'),
    path('delete_user/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
]