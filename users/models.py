from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    number = models.CharField(max_length=30, verbose_name='телефон')
    city = models.CharField(max_length=30, verbose_name='город')
    image = models.ImageField(upload_to='users/', verbose_name='аватар)', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}({self.first_name})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'