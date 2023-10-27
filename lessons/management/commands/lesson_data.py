from django.core.management import BaseCommand

from courses.models import Course
from lessons.models import Lesson
from users.models import User


class Command(BaseCommand):
    """
    Класс уроков.
    """
    def handle(self, *args, **kwargs):
        lesson_list = [
            {
                "name": "1.1 lesson",
                "content": "1 урок 1 куса",
                "course": Course.objects.get(pk=1),
                "name_user": User.objects.get(pk=1)
            },
            {
                "name": "1.2 lesson",
                "content": "2 урок 1 куса",
                "course": Course.objects.get(pk=1),
                "name_user": User.objects.get(pk=2)
            },
            {
                "name": "2.1 lesson",
                "content": "1 урок 2 куса",
                "course": Course.objects.get(pk=2),
                "name_user": User.objects.get(pk=2)
            },
            {
                "name": "2.2 lesson",
                "content": "1 урок 1 куса",
                "course": Course.objects.get(pk=2),
                "name_user": User.objects.get(pk=1)
            },
            {
                "name": "3.1 lesson",
                "content": "1 урок 3 куса",
                "course": Course.objects.get(pk=3),
                "name_user": User.objects.get(pk=3)
            },
            {
                "name": "3.2 lesson",
                "content": "2урок 3 куса",
                "course": Course.objects.get(pk=3),
                "name_user": User.objects.get(pk=1)
            }
        ]

        lesson_for_create = []
        for lesson_item in lesson_list:
            lesson_for_create.append(
                Lesson(**lesson_item)
            )

        Lesson.objects.bulk_create(lesson_for_create)
        print(lesson_for_create)
