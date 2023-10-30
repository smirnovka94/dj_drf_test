from rest_framework import serializers

from courses.validators import ContentValidator
from lessons.models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [ContentValidator(field='content')]