from django.urls import path
from .views import chatbot_response, chat_page  # исправили импорт
from .views import OrderCreateView
from .views import latest_order
from . import views
from .views import dish_list
from django.contrib.auth.views import LogoutView



urlpatterns = [
  
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
    path('profile/', views.profile, name='profile'),
    path('api/dishes/', dish_list, name='dish-list'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
