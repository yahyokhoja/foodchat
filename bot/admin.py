# admin.py
from django.contrib import admin
from .models import Order
from django.contrib import admin
from django.utils.html import format_html

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
        'delivery_address', 
        'delivery_cost', 
        'discount', 
        'ordered_by', 
        'received_by', 
        'delivery_duration'
    )
    list_filter = ('status', 'payment_method', 'delivery_method')
    search_fields = ('phone_number', 'order_name', 'ordered_by')
    fieldsets = (
        (None, {
            'fields': ('order_name', 'phone_number', 'status', 'payment_method', 'delivery_method', 'quantity')
        }),
        ('Доставка', {
            'fields': ('delivery_time', 'delivery_address', 'delivery_cost', 'discount', 'delivery_duration')
        }),
        ('Заказчик', {
            'fields': ('ordered_by', 'received_by')
        }),
        ('Прочее', {
            'fields': ('items', 'total_price', 'created_at')
        }),
    )





class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('phone_number',)

admin.site.register(Order, OrderAdmin)
