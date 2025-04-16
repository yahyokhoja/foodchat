from django.db import models
import json

class Order(models.Model):
    user = models.ForeignKey(
        'auth.User', 
        on_delete=models.SET_NULL, 
        null=True,  
        blank=True
    )
    phone_number = models.CharField(max_length=20)
    items = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")

    order_name = models.CharField(max_length=100, default='Без названия')  # Имя заказа
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('card', 'Card')])
    delivery_method = models.CharField(max_length=50, null=True, blank=True, default='pickup')
    quantity = models.PositiveIntegerField(default=1)

    # Новые поля
    delivery_time = models.DateTimeField(null=True, blank=True)  # Время доставки
    delivery_address = models.CharField(max_length=255, null=True, blank=True)  # Адрес доставки
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Стоимость доставки
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Скидка
    ordered_by = models.CharField(max_length=100, null=True, blank=True)  # Кто заказал
    received_by = models.CharField(max_length=100, null=True, blank=True)  # Кто принимает заказ
    delivery_duration = models.DurationField(null=True, blank=True)  # Сколько времени займет доставка

    def __str__(self):
        return f"Заказ {self.id} от {self.phone_number} ({self.order_name})"

    def set_items(self, value):
        self.items = json.dumps(value)

    def get_items(self):
        return json.loads(self.items)
