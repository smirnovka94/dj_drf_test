from django.urls import path
from payments.apps import PaymentsConfig

from payments.views import PaymentCreateAPIView, PaymentListAPIView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
]