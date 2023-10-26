from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс уроков.
    """
    def handle(self, *args, **kwargs):
        users_list = [
            {
                "email": "first_user@mail.ru",
                "number": "123456798",
                "city": 'SPb'
            }
        ]

        users_for_create = []
        for user_item in users_list:
            users_for_create.append(
                User(**user_item)
            )

        User.objects.bulk_create(users_for_create)
        print(users_for_create)

