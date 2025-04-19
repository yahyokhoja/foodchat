import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Dish
from .serializers import DishSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def make_order(request):
    if request.method == 'POST':
        data = request.POST
        print(f"Data received: {data}")  # Выводим данные, полученные в POST запросе

        try:
            items = json.loads(data.get('items'))
            print(f"Items received: {items}")  # Выводим товары из заказа
        except json.JSONDecodeError:
            items = []

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            phone_number=data.get('phone_number'),
            ordered_by=data.get('ordered_by'),
            delivery_address=data.get('delivery_address'),
            payment_method=data.get('payment_method'),
            delivery_method=data.get('delivery_method'),
            created_at=timezone.now(),
        )
        order.items = json.dumps(items)
        order.calculate_total_price()  # Подсчёт + сохранение
        order.save()

        print(f"Order created: {order}")  # Выводим информацию о созданном заказе

        # Очистка localStorage будет на фронте
        return redirect('profile')
    return redirect('checkout')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    print(f"Cart data: {cart}")  # Выводим данные из корзины

    if not cart:
        return redirect('cart')  # Если корзина пуста, редирект на страницу корзины

    total_price = 0
    items = []
    for item in cart.values():
        total_price += float(item['price']) * item['quantity']
        items.append(item)

    order = Order.objects.create(
        user=request.user,
        phone_number=request.user.profile.phone_number,
        items=json.dumps(items),  # Если это строка JSON, все в порядке
        total_price=total_price
    )

    print(f"Order created during checkout: {order}")  # Информация о заказе в процессе оформления

    # Очистить корзину после оформления
    del request.session['cart']

    return render(request, 'bot/checkout.html', {'order': order})

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(f"[add_to_cart] Data received: {data}")

            dish = data.get('dish')
            if not dish:
                return JsonResponse({'status': 'error', 'message': 'Dish not found in request'}, status=400)

            cart = request.session.get('cart', {})
            print(f"[add_to_cart] Cart before: {cart}")

            dish_id = str(dish['id'])

            if dish_id in cart:
                cart[dish_id]['quantity'] += 1
            else:
                cart[dish_id] = {
                    'name': dish['name'],
                    'price': str(dish['price']),
                    'quantity': 1
                }

            request.session['cart'] = cart
            request.session.modified = True  # Важно!
            print(f"[add_to_cart] Cart after: {request.session['cart']}")

            return JsonResponse({'status': 'success', 'cart_count': len(cart)})
        except Exception as e:
            print(f"[add_to_cart] Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)




def index(request):
    dishes = Dish.objects.filter(available=True)[:3]  # Например, только 3 блюда
    print(f"Dishes displayed on index page: {dishes}")  # Выводим блюда на главной странице
    return render(request, "bot/index.html", {"dishes": dishes})

@api_view(['GET'])
def dish_list(request):
    dishes = Dish.objects.filter(available=True)
    print(f"Dishes list: {dishes}")  # Выводим список блюд для API
    serializer = DishSerializer(dishes, many=True, context={'request': request})
    return Response(serializer.data)

def menu(request):
    dishes = Dish.objects.all()
    print(f"Menu dishes: {dishes}")  # Выводим все блюда для меню
    return render(request, 'bot/menu.html', {'dishes': dishes})

class OrderCreateView(APIView):
    def post(self, request):
        order_data = request.data
        print(f"Order data received: {order_data}")  # Выводим полученные данные для заказа

        try:
            for item in order_data['items']:
                Order.objects.create(
                    user_phone=order_data['user'],
                    dish=item['dish'],
                    quantity=item['qty'],
                )
            print(f"Order created successfully.")  # Подтверждаем создание заказа
            return Response({"message": "Заказ успешно создан!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error while creating order: {str(e)}")  # Выводим ошибку, если не удалось создать заказ
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def latest_order(request):
    order = Order.objects.latest('created_at')
    print(f"Latest order: {order}")  # Выводим последний заказ
    return JsonResponse({
        'order_name': order.order_name,
        'phone_number': order.phone_number,
        'items': order.items,
        'total_price': order.total_price,
        'delivery_address': order.delivery_address,
        'delivery_time': order.delivery_time.strftime('%Y-%m-%d %H:%M'),
        'status': order.status,
    })

def chatbot_response(request):
    # Логика ответа бота на запросы
    print("Chatbot response requested.")  # Отладка запроса к боту
    return JsonResponse({"message": "Ответ от бота"})

def chat_page(request):
    return render(request, "bot/chat_page.html")

def cart(request):
    print("Cart page accessed.")  # Выводим информацию о доступе к странице корзины
    return render(request, 'bot/cart.html')

def orders(request):
    print("Orders page accessed.")  # Выводим информацию о доступе к странице заказов
    return render(request, 'bot/orders.html')

def profile(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        print(f"Orders for user {request.user.username}: {orders}")  # Выводим заказы пользователя
    else:
        orders = []

    return render(request, 'bot/profile.html', {'orders': orders})

def search(request):
    query = request.GET.get('q', '')  # Получаем строку запроса
    category = request.GET.get('category', '')  # Получаем выбранную категорию
    results = Dish.objects.all()  # По умолчанию ищем все блюда

    # Фильтрация по названию блюда
    if query:
        results = results.filter(name__icontains=query)

    # Фильтрация по категории
    if category:
        results = results.filter(category__iexact=category)

    print(f"Search results: {results}")  # Выводим результаты поиска
    return render(request, 'bot/search_results.html', {'results': results, 'query': query, 'category': category})

def cart(request):
    cart = request.session.get('cart', {})  # Получаем корзину из сессии
    print(f"Cart loaded from session: {cart}")  # Печать содержимого корзины из сессии

    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    print(f"Total price: {total_price}")  # Вывод общей стоимости корзины

    return render(request, 'bot/cart.html', {'cart': cart, 'total_price': total_price})
