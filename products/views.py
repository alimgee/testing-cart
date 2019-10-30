from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import Product

# Create your views here.
def products(request):
        
    return render(request, 'products/products.html') 

class ProductListView(ListView):
    #template_name = 'products/products.html'  # <app>/<model>_<viewtype>.html
    model = Product
    context_object_name = 'products'
