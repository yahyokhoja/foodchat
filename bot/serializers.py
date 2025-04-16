from rest_framework import serializers
from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'image', 'available']
