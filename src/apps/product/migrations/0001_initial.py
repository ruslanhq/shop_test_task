# Generated by Django 5.1.2 on 2024-10-13 06:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="product_pictures/",
                        verbose_name="Картинка",
                    ),
                ),
                ("content", models.TextField(verbose_name="Контент")),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
            ],
        ),
    ]
