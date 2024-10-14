from rest_framework import serializers

from src.apps.order.api.v1.serializers import OrderSerializer
from src.apps.order.models import Order
from src.apps.payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Order.objects.prefetch_related('products')
    )

    class Meta:
        model = Payment
        fields = ["amount", "status", "type_of_payment", "order", ]
        read_only_fields = ['amount', "status"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order'] = OrderSerializer(instance.order, many=False).data
        return representation
