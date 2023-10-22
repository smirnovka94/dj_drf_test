from rest_framework import serializers
from courses.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from users.models import User, NULLABLE


class CourseSerializer(serializers.ModelSerializer):
    # lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    lessons_count = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['name', 'content', 'lessons_count']

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()


"""
class PaymentsSerializer(serializers.Serializer):
    METODS = [
        ("cash", "Наличные"),
        ("transfer", "Перевод на счет"),
    ]

    name_user = serializers.ForeignKey(User, verbose_name='пользователь')
    data = serializers.DateTimeField(verbose_name='дата оплаты')
    pay_course = serializers.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    pay_lesson = serializers.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    pay = serializers.ImageField(verbose_name='сумма оплаты')
    payment_method = serializers.CharField(max_length=150, choices=METODS, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.pay_course if self.pay_course else self.pay_lesson} - {self.data}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        fields = "__all__"
        ordering = ('-data')
"""