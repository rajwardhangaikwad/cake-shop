from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('cake', 'Cakes'),
        ('pastry', 'Pastries'),
        ('bread', 'Breads'),
        ('cupcake', 'Cupcakes'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cakes/')
    
    category = models.CharField((max_length=20, choices=CATEGORY_CHOICES)
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='cake'
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()