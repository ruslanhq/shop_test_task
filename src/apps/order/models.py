import uuid

from django.db import models
from django.utils import timezone

from src.apps.product.models import Product


class OrderStatus(models.TextChoices):
    PENDING = "Ожидает", "ожидает"
    CONFIRMED = "подтвержден", "Подтвержден"
    CANCELED = "отменен", "Отменен"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Итоговая сумма"
    )
    status = models.CharField(
        max_length=12,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name="Статус",
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Время создания"
    )
    confirmation_time = models.DateTimeField(
        null=True, blank=True, verbose_name="Время подтверждения"
    )
    products = models.ManyToManyField(
        Product, related_name="orders", verbose_name="Продукты"
    )

    def __str__(self):
        return f"Заказ #{self.id} - {self.status}"
