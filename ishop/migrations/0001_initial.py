# Generated by Django 5.0.2 on 2024-03-11 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_image", models.ImageField(upload_to="uploads/category/")),
                (
                    "category_name",
                    models.CharField(default="", max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(default="", max_length=100, null=True)),
                ("last_name", models.CharField(default="", max_length=100, null=True)),
                ("mobile", models.IntegerField(default=1)),
                ("email", models.CharField(default="", max_length=100, null=True)),
                ("password", models.CharField(default="", max_length=100, null=True)),
                ("gender", models.CharField(default="", max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(default="", max_length=100, null=True),
                ),
                ("product_image", models.ImageField(upload_to="uploads/product/")),
                (
                    "product_desc",
                    models.CharField(default="", max_length=300, null=True),
                ),
                ("product_price", models.IntegerField(default=1)),
                (
                    "product_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ishop.category"
                    ),
                ),
            ],
        ),
    ]
