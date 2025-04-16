from django.db import models
import json

class Order(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь"
    )
    phone_number = models.CharField("Номер телефона", max_length=20)
    items = models.TextField("Содержимое заказа")
    total_price = models.DecimalField("Общая стоимость", max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    status = models.CharField("Статус", max_length=20, default="pending")

    order_name = models.CharField("Название заказа", max_length=100, default='Без названия')
    payment_method = models.CharField("Способ оплаты", max_length=50, choices=[('cash', 'Наличные'), ('card', 'Карта')])
    delivery_method = models.CharField("Способ доставки", max_length=50, null=True, blank=True, default='pickup')
    quantity = models.PositiveIntegerField("Количество", default=1)

    delivery_time = models.DateTimeField("Время доставки", null=True, blank=True)
    delivery_address = models.CharField("Адрес доставки", max_length=255, null=True, blank=True)
    delivery_cost = models.DecimalField("Стоимость доставки", max_digits=6, decimal_places=2, default=0.00)
    discount = models.DecimalField("Скидка", max_digits=6, decimal_places=2, default=0.00)
    ordered_by = models.CharField("Кто заказал", max_length=100, null=True, blank=True)
    received_by = models.CharField("Кто принимает", max_length=100, null=True, blank=True)
    delivery_duration = models.DurationField("Длительность доставки", null=True, blank=True)

    def __str__(self):
        return f"Заказ {self.id} от {self.phone_number} ({self.order_name})"

    def set_items(self, value):
        self.items = json.dumps(value)

    def get_items(self):
        return json.loads(self.items)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes_images/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name       
