from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register_view.as_view(), name="register"),
    path("product/", product_view.as_view({'get':'list'}), name="product" ),
    path("allProduct/", allProduct.as_view(), name="allProduct" ),
    path("createProduct/", create_product.as_view(), name="createProduct"),
    path("singleProduct/<int:pk>",updateDelete_product.as_view(), name="single" ),
    path("updateDelete/<int:pk>",updateDelete_product.as_view(), name="updateDelete" ),
]
