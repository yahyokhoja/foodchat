from django.urls import path
from .views import chatbot_response, chat_page  # исправили импорт
from .views import OrderCreateView

urlpatterns = [
    path("chat/", chatbot_response, name="chat"),  # Исправили путь для chatbot_response
   path('api/orders/', OrderCreateView.as_view(), name='create_order'),
]
