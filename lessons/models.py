from django.db import models
from users.models import NULLABLE

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    content = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='blogs/', verbose_name='превью', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

