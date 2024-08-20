from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register_view.as_view(), name="register"),
    path('login/', Login_view.as_view(), name="Login" ),
    path("product/", product_view.as_view({'get':'list'}), name="product" ),
    path("allProduct/", allProduct.as_view(), name="allProduct" ),
    path("createProduct/", create_product.as_view(), name="createProduct"),
    path("singleProduct/<int:pk>",updateDelete_product.as_view(), name="single" ),
    path("updateDelete/<int:pk>",updateDelete_product.as_view(), name="updateDelete" ),
    path("contact/", all_contacts.as_view(), name="contact"),
    path("contact/<int:pk>/", all_contact.as_view(), name="contact"),
    path("category/", categorys.as_view(), name="category"),
    path("addCategory/", categoryAdd.as_view(), name="addCategory"),
    path("category/<int:pk>", category.as_view(), name= "category"),
    path("category/product/<int:id>", ProductCategory.as_view(), name= "ProductCategory"),
]
# Form Handling,
# error handling
# contact, 
# login, register, 
# admin dashboard 
# pip install -r requirements.txt


