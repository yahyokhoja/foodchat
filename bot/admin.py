from django.contrib import admin
from .models import Order
from .models import Dish



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_name',
        'phone_number',
        'total_price',
        'created_at',
        'status',
        'payment_method',
        'delivery_method',
        'quantity',
        'delivery_time',
    )
    list_filter = ('status', 'payment_method', 'delivery_method')
    search_fields = ('phone_number', 'order_name', 'ordered_by', 'received_by')

    readonly_fields = ('created_at',)  # Сделаем created_at только для чтения

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'order_name',
                'phone_number',
                'status',
                'payment_method',
                'delivery_method',
                'quantity',
                'items',
                'total_price',
            )
        }),
        ('Доставка', {
            'fields': (
                'delivery_time',
                'delivery_address',
                'delivery_cost',
                'discount',
                'delivery_duration',
            )
        }),
        ('Участники', {
            'fields': (
                'ordered_by',
                'received_by',
            )
        }),
        ('Системная информация', {
            'fields': (
                'created_at',
            )
        }),
    )



@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'category')
    list_filter = ('available', 'category')
    search_fields = ('name', 'description')



