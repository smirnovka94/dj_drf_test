from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from subscriptions.models import Subscription
from courses.models import Course
from users.models import User


@shared_task
def check_course(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course.id)
    for subscription in subscriptions:

        send_mail(
            subject=f"Обновленине курса {course.name}",
            message=f"Вы получилии это письмо скоскольку подписались на рассылку",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email,]
        )

    # if Subscription.objects.filter(users).exists():

def long_active_user():
    "Проверка юзера на активность, если небыло больше 4 мес то меняется is_active -> False"
    users = User.objects.all()
    for user in users:
        time_user = user.last_login.replace(tzinfo=None)
        time_now = datetime.now().replace(tzinfo=None)
        time_diff = time_now - time_user
        if time_diff > timedelta(days=120):
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()