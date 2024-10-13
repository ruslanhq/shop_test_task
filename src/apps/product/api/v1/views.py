from rest_framework.generics import ListAPIView

from src.apps.product.api.v1.serializers import ProductSerializer
from src.apps.product.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
