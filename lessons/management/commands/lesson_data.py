from django.core.management import BaseCommand

from courses.models import Course
from lessons.models import Lesson

class Command(BaseCommand):
    """
    Класс уроков.
    """
    def handle(self, *args, **kwargs):
        lesson_list = [
            {
                "name": "3.1 lesson",
                "content": "Третий урок третьего",
                "course": Course.objects.get(pk=1)
            }
        ]

        lesson_for_create = []
        for lesson_item in lesson_list:
            lesson_for_create.append(
                Lesson(**lesson_item)
            )

        Lesson.objects.bulk_create(lesson_for_create)
        print(lesson_for_create)
