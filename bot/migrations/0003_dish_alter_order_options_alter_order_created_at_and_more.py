# Generated by Django 5.2 on 2025-04-16 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_delete_dish_order_delivery_address_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='dishes_images/')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Стоимость доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Длительность доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(blank=True, default='pickup', max_length=50, null=True, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.TextField(verbose_name='Содержимое заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(default='Без названия', max_length=100, verbose_name='Название заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_by',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Кто заказал'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличные'), ('card', 'Карта')], max_length=50, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='received_by',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Кто принимает'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Общая стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
