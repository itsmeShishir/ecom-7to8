from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterSerializations(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username'),
            password=validated_data['password']
        )
        return user
# products = ProductSerializer(many=True, read_only=True
# lookup_field = 'id'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # depth = 1

class CategorySerializations(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields= ['id', 'title', 'description', 'img', 'product']

    def get_product(self, obj):
        product = Product.objects.filter(category=obj)
        return ProductSerializer(product, many=True).data
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"