from django.urls import path
from payments.apps import PaymentsConfig
from payments.views import PaymentCreateAPIView, PaymentListAPIView, GetPaymentView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payments/<str:payment_id>/', GetPaymentView.as_view(), name='payment_get'),
]