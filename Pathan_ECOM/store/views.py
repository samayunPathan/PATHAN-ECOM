from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.
def product_details(request,slug):
    product=get_object_or_404(Product,slug=slug)
    return render(request,'store/product_detail.html',{
        'product':product
    })

