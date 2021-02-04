from django.contrib import admin
from django.urls import path
from cart.views import AddToCart


urlpatterns = [
    path('addtocart/', AddToCart, name="AddToCart"),
]