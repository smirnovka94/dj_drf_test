from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class UserRoles(models.TextChoices):
    MEMBER = "member", "Пользователь"
    MODERATOR = "moderator", "Модератор"

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    number = models.CharField(max_length=30, verbose_name='телефон')
    city = models.CharField(max_length=30, verbose_name='город')
    image = models.ImageField(upload_to='users/', verbose_name='аватар)', **NULLABLE)
    last_login = models.DateTimeField(auto_now=True, verbose_name='последний вход', **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}({self.first_name, self.last_login, self.is_active})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'