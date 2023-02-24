#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# from userprofile.models import BecomeVendor
from userprofile.models import BecomeVendor

User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='uploads/category/', blank=True, null=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETEED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'waitingapproval'),
        (ACTIVE, 'active'),
        (DELETEED,  'deleted')
    )

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)  #vendor who added product
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/product_images/', null=True)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    sold = models.IntegerField(blank=True, null=True,default=0)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Vendor(models.Model):
    ACTIVE = 'active'
    DELETEED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (DELETEED,  'deleted')
    )
    user = models.ForeignKey(User, related_name='vendors', on_delete=models.CASCADE)
    no_of_product = models.IntegerField()
    income = models.IntegerField()
    joined_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    
    def __str__(self):
        return self.user.first_name


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=50)
    mobile = models.CharField(max_length=15, null=True, blank= True)
    address = models.TextField(blank=True)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=255)
    payement_intent = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name  # change this to created_b if possible

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    total = models.IntegerField()           

    def __str__(self):
        return self.product.title

    def get_display_price(self):
        return self.price / 100










