from django.urls import path

from src.apps.payment.api.v1.views import PaymentCreateView

urlpatterns = [
    path("api/v1/create_payment/", PaymentCreateView.as_view(), name="create_payment"),
]
