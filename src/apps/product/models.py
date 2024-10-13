import os
import uuid

from django.db import models


def rename_uploaded_image(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('product_pictures/', new_filename)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, verbose_name='Название')
    picture = models.ImageField(upload_to=rename_uploaded_image, null=True, blank=True, verbose_name='Картинка')
    content = models.TextField(verbose_name='Контент')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return self.name
