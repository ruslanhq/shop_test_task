from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status, generics

from src.apps.order.api.v1.serializers import OrderSerializer
from src.apps.order.api.v1.services import OrderService


class OrderCreateView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=OrderSerializer,
        responses={201: OrderSerializer(), 400: "Bad Request"},
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        products = serializer.validated_data['products']
        service = OrderService()

        try:
            order = service.create_order(products)
            serializer.instance = order
        except ValueError as e:
            raise serializer.ValidationError({'detail': str(e)})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
