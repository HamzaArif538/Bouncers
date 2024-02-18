from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def products(request):
    product = Product.objects.all()
    totalproducts = product.count()

    sort_option  = request.GET.get('sort', None)

    if sort_option == 'price_low':
        product = product.order_by('price')
    elif sort_option == 'price_high':
        product = product.order_by('-price')
    elif sort_option == 'name_asc':
        product = product.order_by('name')
    elif sort_option == 'name_desc':
        product = product.order_by('-name')
    elif sort_option == 'latest':
        product = product.order_by('-date_created')
    elif sort_option == 'oldest':
        product = product.order_by('date_created')
        

    for item in product:
        # Handle potential null values gracefully to avoid errors
        if item.oldprice and item.price:
            percentoff = round(((item.oldprice - item.price) / item.oldprice) * 100, 0)
            
        else:
            percentoff = None  # Set to None if price or oldprice is missing

        item.percentoff = percentoff

    category_filter = request.GET.get('category', None)
    if category_filter == 'all_cats':
        pass
    elif category_filter == 'loafers':
        product = product.filter(category='Loafers')
    elif category_filter == 'peshawari':
        product = product.filter(category='Peshawari')
    elif category_filter == 'formal':
        product = product.filter(category='Formal Shoes')
    elif category_filter == 'khussa':
        product = product.filter(category='Khussa')
    elif category_filter == 'heels':
        product = product.filter(category='High Heels')

    
    page = request.GET.get('page', 1)
    paginator = Paginator(product, 8)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    context = {'product':product, 'totalproducts':totalproducts,
            'percentoff':percentoff}
    return render(request, 'core/products.html', context)

def productdetail(request):
    context = {}
    return render(request, 'core/productdetails.html', context)

def aboutus(request):
    context = {}
    return render(request, 'core/aboutus.html', context)

def contactus(request):
    context = {}
    return render(request, 'core/contactus.html', context)