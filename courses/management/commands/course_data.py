from django.core.management import BaseCommand

from courses.models import Course


class Command(BaseCommand):
    """
    Класс курсов.
    """

    def handle(self, *args, **kwargs):
        course_list = [
            {
                "name": "Третий курс",
                "content": "описание третьего курс"
            },
            {
                "name": "Четвертый курс",
                "content": "описание 4 курса"
            },

        ]

        course_for_create = []
        for course_item in course_list:
            course_for_create.append(
                Course(**course_item)
            )

        Course.objects.bulk_create(course_for_create)
        print(course_for_create)
