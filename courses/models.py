from django.conf import settings
from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    content = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='blogs/', verbose_name='превью', **NULLABLE)
    name_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курc'
        verbose_name_plural = 'курсы'

