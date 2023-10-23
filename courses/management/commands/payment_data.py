from django.core.management import BaseCommand

from courses.models import Course, Payments
from lessons.models import Lesson
from users.models import User


class Command(BaseCommand):
    """
    Класс оплаты.
    """

    def handle(self, *args, **kwargs):
        payment_list = [
            {
                "name_user": User.objects.get(pk=1),
                "data": "2023-09-09",
                "pay_course": Course.objects.get(pk=2),
                "pay": "1000",
                "payment_method": "cash",
            },
            {
                "name_user": User.objects.get(pk=1),
                "data": "2023-10-10",
                "pay_lesson": Lesson.objects.get(pk=1),
                "pay": "500",
                "payment_method": "transfer",
            },
        ]

        payment_for_create = []
        for pay_item in payment_list:
            payment_for_create.append(
                Payments(**pay_item)
            )

        Payments.objects.bulk_create(payment_for_create)
        print(payment_for_create)
