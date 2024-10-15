from django.urls import path

from src.apps.order.api.v1.views import OrderCreateView

urlpatterns = [
    path("api/v1/create_order/", OrderCreateView.as_view(), name="create_order"),
]
