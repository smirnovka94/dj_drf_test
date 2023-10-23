from rest_framework import viewsets, generics

from courses.models import Course, Payments
from courses.serializers import CourseSerializer, PaymentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer