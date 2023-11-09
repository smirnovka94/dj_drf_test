from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from subscriptions.models import Subscription
from courses.models import Course


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
@shared_task
def check_filter():
    subscribed_courses = Course.objects.filter(subscription__is_active=True)
    for course in subscribed_courses:
        print(course.name)