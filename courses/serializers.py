from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from courses.models import Course, Payments
from courses.validators import ContentValidator
from lessons.models import Lesson
from subscriptions.serializers import SubscriptionSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()
    lessons_count = SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        validators = [ContentValidator(field='content')]

    def get_lessons(self, obj):
        """Получаем список уроков курса"""
        lessons = Lesson.objects.filter(course=obj)
        return [lesson.name for lesson in lessons]
    def get_lessons_count(self, instance):
        """Получаем количество уроков в курсе"""
        return instance.lesson_set.count()

    def get_is_subscribed(self, obj):
        """Получаем статус подписки в курсе - если подписка активирована текущим пользователем"""
        request_user = self.context.get('user')
        subscription = obj.subscription_set.filter(user=request_user).first()
        if subscription:
            return subscription.is_active
        return False



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class PaymentlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'