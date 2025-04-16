# foodchat/urls.py

from django.contrib import admin
from django.urls import path
from bot import views  # Импортируем представления из вашего приложения 'bot'

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к админке Django
    path('', views.index, name='index'),  # Главная страница, которая будет использовать index.html
    # Здесь вы можете добавить другие маршруты, если необходимо
]
