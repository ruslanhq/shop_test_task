import uuid

from django.db import models

from src.apps.order.models import Order


class PaymentStatus(models.TextChoices):
    PAID = 'Оплачен', 'оплачен'
    UNPAID = 'Не оплачен', 'не оплачен'
    IN_PROCESS = 'В обработке', 'в обработке'


class PaymentType(models.TextChoices):
    CREDIT_CARD = 'Безналичные', 'безналичные'
    Cash = 'Наличные', 'наличные'


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма", blank=True)
    status = models.CharField(max_length=12, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID, verbose_name="статус")
    type_of_payment = models.CharField(max_length=20, choices=PaymentType.choices, verbose_name="тип оплаты")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment', verbose_name="заказ")

    def __str__(self):
        return f"Платеж к Заказу #{self.order.id}"

    def save(self, *args, **kwargs):
        if self.amount != self.order.total:
            self.amount = self.order.total
        super().save(*args, **kwargs)
