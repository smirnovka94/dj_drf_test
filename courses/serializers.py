from rest_framework import serializers
from courses.models import Course, Payments
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


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
