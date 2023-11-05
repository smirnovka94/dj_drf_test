from rest_framework import serializers

from payments.models import Payments

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class PaymentlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'