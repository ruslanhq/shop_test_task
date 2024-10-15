from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import path
from django.utils import timezone


from src.apps.order.api.v1.services import OrderService
from src.apps.order.models import Order, OrderStatus
from src.apps.payment.models import PaymentStatus


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "total",
        "status",
        "created_at",
        "confirmation_time",
    )
    readonly_fields = (
        "total",
        "created_at",
        "confirmation_time",
    )
    fields = (
        "total",
        "status",
        "products",
        "created_at",
        "confirmation_time",
    )
    change_form_template = "admin/order_change_form.html"

    def save_model(self, request, obj, form, change):
        products = form.cleaned_data.get("products")

        if products:
            total = OrderService.calculate_total(products)
            obj.total = total

        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<path:object_id>/confirm_order/",
                self.admin_site.admin_view(self.confirm_order),
                name="confirm_order",
            ),
        ]
        return custom_urls + urls

    def confirm_order(self, request, object_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=object_id)
        payment = getattr(order, "payment", None)

        if (
            payment
            and payment.status == PaymentStatus.PAID
            and order.status != OrderStatus.CONFIRMED
        ):
            order.status = OrderStatus.CONFIRMED
            order.confirmation_time = timezone.now()
            order.save()
            messages.success(request, "Заказ был подтвержден.")

            # Запускаем Celery задачу для отправки Post-запроса
            from src.apps.order.tasks import process_order_confirmation

            process_order_confirmation.delay(str(order.id))

            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(
                request, "Платеж не имеет статус 'Оплачен' или заказ уже подтвержден."
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    def render_change_form(self, request, context, *args, **kwargs):
        obj = context.get("original")
        payment = getattr(obj, "payment", None)
        show_confirm_button = False

        if (
            obj
            and payment
            and payment.status == PaymentStatus.PAID
            and obj.status != OrderStatus.CONFIRMED
        ):
            show_confirm_button = True

        context["show_confirm_button"] = show_confirm_button
        return super().render_change_form(request, context, *args, **kwargs)
