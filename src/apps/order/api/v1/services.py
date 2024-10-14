from src.apps.order.models import Order
from src.apps.product.models import Product


class OrderService:
    @staticmethod
    def calculate_total(products: list[Product]):
        return sum(product.cost for product in products)

    def create_order(self, products: list[Product]):
        total = self.calculate_total(products)
        order = Order.objects.create(total=total)
        order.products.set(products)
        return order
