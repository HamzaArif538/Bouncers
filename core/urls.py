from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('products', views.products, name='products' ),
    path('productdetail', views.productdetail, name='productdetail'),


    path('aboutus', views.aboutus, name='aboutus' ),
    path('contactus', views.contactus, name='contactus' ),
]
