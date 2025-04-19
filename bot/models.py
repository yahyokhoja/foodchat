from django.db import models
import json

# Модель Заказа
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
    ]
    DELIVERY_METHOD_CHOICES = [
        ('pickup', 'Самовывоз'),
        ('delivery', 'Доставка'),
    ]

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь"
    )
    phone_number = models.CharField("Номер телефона", max_length=20)
    items = models.TextField("Содержимое заказа", blank=True, default="[]")
    total_price = models.DecimalField("Общая стоимость", max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="pending")
    order_name = models.CharField("Название заказа", max_length=100, default='Без названия')
    payment_method = models.CharField("Способ оплаты", max_length=50, choices=PAYMENT_METHOD_CHOICES)
    delivery_method = models.CharField("Способ доставки", max_length=50, choices=DELIVERY_METHOD_CHOICES, default='pickup')
    delivery_time = models.DateTimeField("Время доставки", null=True, blank=True)
    delivery_address = models.CharField("Адрес доставки", max_length=255, null=True, blank=True)
    delivery_cost = models.DecimalField("Стоимость доставки", max_digits=6, decimal_places=2, default=0.00)
    discount = models.DecimalField("Скидка", max_digits=6, decimal_places=2, default=0.00)
    ordered_by = models.CharField("Кто заказал", max_length=100, null=True, blank=True)
    received_by = models.CharField("Кто принимает", max_length=100, null=True, blank=True)
    delivery_duration = models.DurationField("Длительность доставки", null=True, blank=True)

    def __str__(self):
        return f"Заказ {self.id} от {self.phone_number} ({self.order_name})"

    def get_items(self):
        if not self.items:
            return []
        try:
            return json.loads(self.items)
        except json.JSONDecodeError:
            return []

    def set_items(self, value):
        self.items = json.dumps(value)

    def calculate_total_price(self):
        total = 0
        for item in self.get_items():
            total += float(item['price']) * item['quantity']
        total += float(self.delivery_cost)
        total -= float(self.discount)
        self.total_price = total
        self.save()

    def add_item(self, dish, quantity=1):
        items = self.get_items()
        for item in items:
            if item['dish_id'] == dish.id:
                item['quantity'] += quantity
                self.set_items(items)
                return
        items.append({'dish_id': dish.id, 'name': dish.name, 'price': str(dish.price), 'quantity': quantity})
        self.set_items(items)
        self.save()

    def update_item(self, dish, quantity):
        items = self.get_items()
        for item in items:
            if item['dish_id'] == dish.id:
                item['quantity'] = quantity
                self.set_items(items)
                self.save()
                return

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


# Модель Блюдо
class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('osh', 'Ош'),
        ('kabob', 'Кабоб'),
        ('salad', 'Салат'),
        ('desert', 'Десерт'),
        ('drink', 'Нӯшокиҳо'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes_images/')
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='osh')

    def __str__(self):
        return self.name


# Промежуточная модель (необязательна, если ты не используешь её в логике)
class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.dish.name} (x{self.quantity})"
