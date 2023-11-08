from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from courses.models import Course


@shared_task
def check_course(name_course, email):

    email = 'lekseich8@mail.ru' #Кому отправлять
    send_mail(
        subject=f"Обновленине курса {name_course}",
        message=f"Вы получилии это письмо скоскольку подписались на рассылку",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )

    # if Subscription.objects.filter(users).exists():
@shared_task
def check_filter():
    subscribed_courses = Course.objects.filter(subscription__is_active=True)
    for course in subscribed_courses:
        print(course.name)