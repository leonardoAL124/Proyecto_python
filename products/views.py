from django.shortcuts import render
from .models import Products

# Create your views here.
def products(request):
    products = Products.objects.all()
    return render(request, "products/products.html", {'products':products})