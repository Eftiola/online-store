# Generated by Django 4.1.1 on 2022-09-21 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_remove_orderline_product_remove_orderline_user_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="author",
            new_name="user",
        ),
    ]