from django.contrib import admin

from src.apps.order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'total',
        'status',
        'created_at',
        'confirmation_time',
    )
    readonly_fields = (
        'total',
        'created_at',
        'confirmation_time'
    )
    fields = (
        'total',
        'status',
        'products',
        'created_at',
        'confirmation_time'
    )
