from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from courses.models import Course
from courses.tasks import check_course
from courses.validators import ContentValidator
from lessons.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()
    lessons_count = SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    sending_mail = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        # validators = [ContentValidator(field='content')]

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

    def get_sending_mail(self, obj):
        """получаем дату создания рассылки и дату содания курса"""
        request_user = self.context.get('user')#объект юзера
        name_course = obj.name
        subscription = obj.subscription_set.filter(user=request_user).first() #объект рассылки

        data_subscription = subscription.data_subscription
        data_course = obj.data_course
        if data_subscription<data_course:
            check_course.delay(name_course, request_user.email)
            return 'send_mail'
        return f"data_subscription{data_subscription} --- data_course{data_course}"