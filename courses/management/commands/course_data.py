from django.core.management import BaseCommand

from courses.models import Course
from users.models import User


class Command(BaseCommand):
    """
    Класс курсов.
    """

    def handle(self, *args, **kwargs):
        course_list = [
            {
                "name": "Первый курс",
                "content": "описание 1 курса",
                "name_user": User.objects.get(pk=1)
            },
            {
                "name": "Второй курс",
                "content": "описание 2 курса",
                "name_user": User.objects.get(pk=2)
            },
            {
                "name": "Третий курс",
                "content": "описание третьего курс",
                "name_user": User.objects.get(pk=2)
            },
            {
                "name": "Четвертый курс",
                "content": "описание 4 курса",
                "name_user": User.objects.get(pk=3)
            },

        ]

        course_for_create = []
        for course_item in course_list:
            course_for_create.append(
                Course(**course_item)
            )

        Course.objects.bulk_create(course_for_create)
        print(course_for_create)
