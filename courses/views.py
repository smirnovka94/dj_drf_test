from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from courses.models import Course, Payments
from courses.serializers import CourseSerializer, PaymentSerializer
from users.permissions import IsOwner, IsModerator, IsNotModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner | IsModerator]
        elif self.action in ['destroy']:
            self.permission_classes = [IsOwner]
        elif self.action in ['create']:
            self.permission_classes = [IsNotModerator]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_course', 'pay_lesson', 'payment_method')
    ordering_fields = ('data',)

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

