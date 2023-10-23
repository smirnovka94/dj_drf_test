from django.urls import path

from rest_framework.routers import DefaultRouter
from courses.apps import CoursesConfig
from courses.views import CourseViewSet, PaymentCreateAPIView, PaymentListAPIView

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='lesson_create'),
    path('payment/', PaymentListAPIView.as_view(), name='lesson_list'),
] + router.urls
