from django.conf import settings
from django.db import models

from courses.models import Course
from users.models import NULLABLE, User

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    is_active = models.BooleanField(default=True, verbose_name='активна')
    data_subscription = models.DateTimeField(auto_now_add=True, verbose_name='дата активации подписки',**NULLABLE)

    def __str__(self):
        return f'Подписка на курс {self.course} для пользователя {self.user}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'