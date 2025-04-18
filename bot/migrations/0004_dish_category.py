# Generated by Django 5.2 on 2025-04-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0003_dish_alter_order_options_alter_order_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="category",
            field=models.CharField(
                choices=[
                    ("osh", "Ош"),
                    ("kabob", "Кабоб"),
                    ("salad", "Салат"),
                    ("desert", "Десерт"),
                    ("drink", "Нӯшокиҳо"),
                ],
                default="osh",
                max_length=50,
            ),
        ),
    ]
