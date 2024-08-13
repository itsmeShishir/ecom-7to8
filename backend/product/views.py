from urllib import response
from django.shortcuts import render
from .serialization import *
from rest_framework import generics, viewsets, permissions, status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

User = get_user_model()

# Create your views here.
class Register_view(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializations

class Login_view(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "email": email,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class product_view(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class allProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class create_product(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class updateDelete_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
#contact
class all_contacts(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class all_contact(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

#Category
#GET, POST
class categorys(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializations

#Retrive, Update , Delete
class category(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializations

    
