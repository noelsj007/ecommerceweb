from django.contrib import admin
from accounts.models import UserRegister, AddToCart, Order, Product
# Register your models here.

admin.site.register(UserRegister)
admin.site.register(AddToCart)
admin.site.register(Order)
admin.site.register(Product)