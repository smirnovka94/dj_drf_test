from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics

from courses.models import Course, Payments
from courses.serializers import CourseSerializer, PaymentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_course', 'pay_lesson', 'payment_method')
    ordering_fields = ('data',)

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

