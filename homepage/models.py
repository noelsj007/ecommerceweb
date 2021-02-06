from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL
class Item(models.Model):
    item_name = models.CharField(max_length=1024)
    item_image = models.ImageField(upload_to = 'None')
    item_price = models.PositiveIntegerField()
    item_publisher = models.CharField(max_length=1024)
    item_origin = models.CharField(max_length=1024)
    item_description = models.TextField()
    item_slug = models.SlugField() 

    def __str__(self):
        return self.item_name



class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
