import stripe
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import STRIPE_SECRET_KEY
from payments.models import Payments

from payments.serializers import PaymentSerializer


stripe.api_key = STRIPE_SECRET_KEY


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_course', 'pay_lesson', 'payment_method')
    ordering_fields = ('data',)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pay = serializer.validated_data.get('pay')

        payment_intent = stripe.PaymentIntent.create(
            amount=pay,
            currency='usd',
            payment_method_types=['card'],
        )
        payment_intent.save()

        return Response({"id_stripe": payment_intent.id}, status=status.HTTP_201_CREATED)



class GetPaymentView(APIView):
    """Получение информации о платеже."""

    def get(self, request, payment_id):
        """Получает информацию о платеже по его ID."""
        stripe.api_key = STRIPE_SECRET_KEY
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return JsonResponse(payment_intent.to_dict())



