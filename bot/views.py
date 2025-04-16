# bot/views.py

from django.shortcuts import render

def index(request):
    # Это представление рендерит шаблон 'index.html'
    return render(request, "bot/index.html")
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order

class OrderCreateView(APIView):
    def post(self, request):
        order_data = request.data
        for item in order_data['items']:
            Order.objects.create(
                user_phone=order_data['user'],
                dish=item['dish'],
                quantity=item['qty'],
            )
        return Response({"message": "Заказ успешно создан!"}, status=status.HTTP_201_CREATED)
