# bot/views.py
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import DishSerializer
from .models import Dish

def index(request):
    dishes = Dish.objects.filter(available=True)[:3]  # например, только 3 блюда
    return render(request, "bot/index.html", {"dishes": dishes})



@api_view(['GET'])
def dish_list(request):
    dishes = Dish.objects.filter(available=True)
    serializer = DishSerializer(dishes, many=True, context={'request': request})
    return Response(serializer.data)



def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'bot/menu.html', {'dishes': dishes})

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

def latest_order(request):
    order = Order.objects.latest('created_at')
    return JsonResponse({
        'order_name': order.order_name,
        'phone_number': order.phone_number,
        'items': order.items,
        'total_price': order.total_price,
        'delivery_address': order.delivery_address,
        'delivery_time': order.delivery_time.strftime('%Y-%m-%d %H:%M'),
        'status': order.status,
    })

# bot/views.py
from django.http import JsonResponse

def chatbot_response(request):
    # Здесь будет логика ответа бота на запросы
    return JsonResponse({"message": "Ответ от бота"})


def chat_page(request):
    # Это представление рендерит шаблон 'chat_page.html'
    return render(request, "bot/chat_page.html")

from django.shortcuts import render

def cart(request):
    return render(request, 'bot/cart.html')

from django.shortcuts import render

def orders(request):
    return render(request, 'bot/orders.html')

from django.shortcuts import render

def profile(request):
    return render(request, 'bot/profile.html')



