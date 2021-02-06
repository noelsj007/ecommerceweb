from django.shortcuts import render
# Create your views here.
from cart.models import Product
from homepage.models import Item

def AddToCart(request):
    cartItem = Item.objects.get(pk = Product_id)
    print("product id", Product_id)
    cartItem = Item()
    cartItem = Item.objects.filter(id=product_id)
    
    
    return render(request, 'dropdown.html')
    
