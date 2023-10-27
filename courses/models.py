from django.db import models


from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    content = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='blogs/', verbose_name='превью', **NULLABLE)
    name_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курc'
        verbose_name_plural = 'курсы'


from lessons.models import Lesson
class Payments(models.Model):
    METODS = [
        ("cash", "Наличные"),
        ("transfer", "Перевод на счет"),
    ]

    name_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    data = models.DateTimeField(verbose_name='дата оплаты')
    pay_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплата за курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплата за урок', **NULLABLE)
    pay = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=150, choices=METODS, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.pay_course if self.pay_course else self.pay_lesson} - {self.data}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
