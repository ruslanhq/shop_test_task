from django.contrib import admin
from django.utils.safestring import mark_safe

from src.apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'get_image',
    )
    readonly_fields = (
        'id',
    )

    def get_image(self, object):
        if object.picture:
            return mark_safe(f'<img src="{object.picture.url}" width=50>')
        return '#'

    get_image.short_description = 'Картинка'
