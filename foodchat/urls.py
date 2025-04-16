# foodchat/urls.py
from django.contrib import admin
from django.urls import path, include
from bot import views  # Импортируем представления из приложения 'bot'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к админке Django
    path('', views.index, name='index'),  # Главная страница
    path('api/', include('bot.urls')),  # Подключаем urls из bot под /api/
    path('', include('bot.urls')),  # Подключаем urls приложения bot
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
