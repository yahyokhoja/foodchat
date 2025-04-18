# foodchat/urls.py

from django.contrib import admin
from django.urls import path, include
from bot import views  # если index в views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger схема
schema_view = get_schema_view(
    openapi.Info(
        title="Foodchat API",
        default_version='v1',
        description="Документация для API проекта",
        contact=openapi.Contact(email="yahyokhoja@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),      # Главная страница
    path('api/', include('bot.urls')),        # Все API эндпоинты (например, /menu/)
    
    # Swagger документация
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление настроек для медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
