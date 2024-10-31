from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Почта")
    avatar = models.ImageField(upload_to='users_photo/', verbose_name="Аватар", blank=True, null=True)

    tg_chat_id = models.CharField(max_length=20, verbose_name="Chat id telegramm", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
