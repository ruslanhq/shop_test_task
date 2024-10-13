from django.urls import path

from src.apps.product.api.v1.views import ProductListView

urlpatterns = [
    path('api/v1/products/', ProductListView.as_view(), name='product-list'),
]
