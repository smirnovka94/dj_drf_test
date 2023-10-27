from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс уроков.
    """
    def handle(self, *args, **kwargs):
        user = User.objects.create(
        email='2_user@mail.ru',
        first_name = '2_user',
        number='123456789',
        city='spb',
        )

        user.set_password("qwerty88")
        user.save()

