from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='charging_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='charging_user_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(("category_img"), upload_to=None, height_field=None, width_field=None, max_length=None)
    username = models.ForeignKey(CustomUser,blank = True, null= True , on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"


class Contact(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField(blank= True, null=True)
    description = models.TextField()
    number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Brand = models.CharField(max_length=255)
    img = models.ImageField(upload_to="product/", height_field=None, width_field=None, max_length=None, blank= True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"
   


