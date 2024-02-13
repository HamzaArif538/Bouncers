from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def products(request):
    product = Product.objects.all()
    totalproducts = Product.objects.count()

    for item in product:
        # Handle potential null values gracefully to avoid errors
        if item.oldprice and item.price:
            percentoff = round(((item.oldprice - item.price) / item.oldprice) * 100, 0)
            
        else:
            percentoff = None  # Set to None if price or oldprice is missing

        item.percentoff = percentoff
    
    context = {'product':product, 'totalproducts':totalproducts, 'percentoff':percentoff}
    return render(request, 'core/products.html', context)

def aboutus(request):
    context = {}
    return render(request, 'core/aboutus.html', context)

def contactus(request):
    context = {}
    return render(request, 'core/contactus.html', context)