from django.contrib import admin

from src.apps.payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("get_order_id", "amount", "status", "type_of_payment")
    list_editable = ("status",)
    readonly_fields = ("amount",)

    def get_order_id(self, obj):
        return f"Заказ # {obj.order.id}"

    get_order_id.short_description = "Номер заказа"

    def save_model(self, request, obj, form, change):
        obj.amount = obj.order.total
        super().save_model(request, obj, form, change)
