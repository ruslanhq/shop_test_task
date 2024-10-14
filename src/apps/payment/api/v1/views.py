from rest_framework import generics

from src.apps.payment.api.v1.serializers import PaymentSerializer
from src.apps.payment.models import Payment


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
