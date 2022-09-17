# Generated by Django 4.1.1 on 2022-09-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_remove_order_total_cost_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="role",
            field=models.CharField(
                choices=[("ADMIN", "Admin"), ("USER", "User")],
                default="User",
                max_length=50,
                null=True,
            ),
        ),
    ]