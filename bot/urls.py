from django.urls import path
from .views import chatbot_response, chat_page  # исправили импорт
from .views import OrderCreateView
from .views import latest_order
from . import views
urlpatterns = [
  
    path('orders/', OrderCreateView.as_view(), name='create_order'),
    path('latest-order/', latest_order, name='latest_order'),
    path('menu/', views.menu, name='menu'),
]
