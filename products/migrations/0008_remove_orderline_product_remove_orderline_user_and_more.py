# Generated by Django 4.1.1 on 2022-09-18 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_rename_photo_product_image_rename_title_product_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderline",
            name="product",
        ),
        migrations.RemoveField(
            model_name="orderline",
            name="user",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderLine",
        ),
    ]
