from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    """product_image = models.ImageField(upload_to='cartImg')"""
    product_price = models.IntegerField()
    product_publisher = models.CharField(max_length=100, null=True)
    product_order_date = models.DateField(auto_now=True)
    product_quantity = models.PositiveIntegerField()

