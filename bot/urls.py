
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from bot.views_webhook import github_webhook


urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('menu/', views.menu, name='menu'),  # Меню
    path('orders/', views.orders, name='orders'),  # Страница заказов
    path('cart/', views.cart, name='cart'),  # Корзина
    path('profile/', views.profile, name='profile'),  # Профиль
    path('latest_order/', views.latest_order, name='latest_order'),  # Последний заказ
    path('chat/', views.chat_page, name='chat'),  # Страница чата
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),  # Ответ бота
    path('search/', views.search, name='search'),  # Маршрут для поиска
    path('logout/', LogoutView.as_view(), name='logout'),  # Выход
    path('checkout/', views.checkout, name='checkout'),  # Оформление заказа
    path('make_order/', views.make_order, name='make_order'),  # Обработка оформления заказа
    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),  # Добавление блюда в корзину
  


    path('webhook/', github_webhook),  # теперь webhook доступен по /webhook/
]


