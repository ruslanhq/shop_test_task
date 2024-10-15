from rest_framework import serializers

from src.apps.order.models import Order
from src.apps.product.api.v1.serializers import ProductSerializer
from src.apps.product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "products",
            "total",
            "status",
            "created_at",
            "confirmation_time",
        ]
        read_only_fields = ["id", "total", "status", "created_at", "confirmation_time"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["products"] = ProductSerializer(
            instance.products.all(), many=True
        ).data
        return representation
