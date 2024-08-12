from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterSerializations(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("id","email", "username", "password")
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validation_data):
            user = User.objects.create_user(
                email= validation_data['email'],
                username= validation_data['username'],
                password= validation_data['password'],
            )
            return user
        

class CategorySerializations(serializers.ModelSerializer):
    class Meta:
        models=Category
        fields= "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'Brand', 'img', 'price', 'is_slider', 'is_featured']