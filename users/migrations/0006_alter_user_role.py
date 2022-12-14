# Generated by Django 4.1.1 on 2022-09-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("ADMIN", "Admin"), ("USER", "User")],
                default="User",
                max_length=50,
                null=True,
            ),
        ),
    ]
