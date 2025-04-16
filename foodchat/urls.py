from django.contrib import admin
from django.urls import path, include
from bot import views  # если index в views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),      # Главная страница
    path('', include('bot.urls')),            # Все страницы frontend (например, /menu/)
  
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
