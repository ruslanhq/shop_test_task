from rest_framework.serializers import ModelSerializer

from src.apps.product.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'picture', 'content', 'cost',]
