from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def products(request):
    context = {}
    return render(request, 'core/products.html', context)

def aboutus(request):
    context = {}
    return render(request, 'core/aboutus.html', context)

def contactus(request):
    context = {}
    return render(request, 'core/contactus.html', context)