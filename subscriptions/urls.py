from django.urls import path

from subscriptions.apps import SubscriptionsConfig
from subscriptions.views import SubscriptionCreateAPIView, SubscriptionListAPIView, SubscriptionRetrieveAPIView, SubscriptionUpdateAPIView, \
    SubscriptionDestroyAPIView

app_name = SubscriptionsConfig.name

urlpatterns = [
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscription/<int:pk>/', SubscriptionRetrieveAPIView.as_view(), name='subscription_get'),
    path('subscription/update/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='subscription_update'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
]

