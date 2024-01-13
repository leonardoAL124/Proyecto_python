from django.shortcuts import render
from .models import Benefits, Blog, Display_products, Indications

# Create your views here.
""" def home(request):
    home_benef = Benefits.objects.all()
    home_blog = Blog.objects.all()
    home_prods = Display_products.objects.all()
    home_inds = Indications.objects.all()
    return render(request, "home/home.html", {'products':home_prods}) """

def home(request):
    home_benef = Benefits.objects.all()
    home_blog = Blog.objects.all()
    home_inds = Indications.objects.all()
    return render(request, "home/home.html", {'blogs':home_blog})