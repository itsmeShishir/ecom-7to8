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


class categoryAdd(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Retrive, Update , Delete
class category(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializations

class ProductCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializations
    lookup_field = 'id'

#cart and other
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart=cart)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, cart=cart)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        order = Order.objects.get(user=self.request.user)
        return OrderItem.objects.filter(order=order)

class CreateOrderView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=request.user)
            order = Order.objects.create(user=request.user, cart=cart)
            cart_items = cart.items.all()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            
            cart.items.all().delete()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Cart.DoesNotExist:
            return Response({"error": "No active cart found"}, status=status.HTTP_400_BAD_REQUEST)


    
