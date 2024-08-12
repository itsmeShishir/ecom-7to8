from django.contrib import admin
from .models import Category, Contact, CustomUser, Product
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Product)