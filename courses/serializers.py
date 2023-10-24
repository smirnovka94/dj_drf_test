from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from courses.models import Course, Payments
from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from users.models import User, NULLABLE


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()
    lessons_count = SerializerMethodField()

    def get_lessons(self, obj):
        lessons = Lesson.objects.filter(course=obj)
        return [lesson.name for lesson in lessons]
    def get_lessons_count(self, instance):
        return instance.lesson_set.count()


    class Meta:
        model = Course
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
