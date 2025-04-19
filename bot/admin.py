from django.contrib import admin
from .models import Order, Dish, OrderDish

class OrderDishInline(admin.TabularInline):
    model = OrderDish
    extra = 0
    fields = ('dish', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone_number', 'order_name', 'payment_method', 'status',
        'total_price', 'delivery_method', 'get_total_quantity', 'created_at'
    )
    inlines = [OrderDishInline]

    def get_total_quantity(self, obj):
        return sum(od.quantity for od in OrderDish.objects.filter(order=obj))
    get_total_quantity.short_description = "Всего блюд"

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'available')



