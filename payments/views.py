from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics


from payments.models import  Payments

from payments.serializers import PaymentSerializer

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_course', 'pay_lesson', 'payment_method')
    ordering_fields = ('data',)

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
