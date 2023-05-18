from django.shortcuts import render

from .models import *
from .forms import *

def index(request):
    url = 'index.html'

    return render(request, url)

def about(request):
    url = 'about.html'

    return render(request, url)

def contacts(request):
    url = 'contacts.html'

    return render(request, url)

def warehouse(request):
    url = 'warehouse.html'
                
    return render(request, url, {"wh":Warehouse.objects.all()})

def vendors(request):
    url = 'vendors.html'
    
    vendor = Vendor()
    
    if request.method == "POST":
        form = AddVendor(request.POST)

        if form.is_valid():
            title = form['title'].value()

            vendor.title = title
            vendor.save()
            
    return render(request, url, {"vendors":Vendor.objects.all(), "form":AddVendor(), "vendorsCount":Vendor.objects.count()})

def products(request):
    url = 'products.html'

    product = Product()
    
    if request.method == "POST":
        form = AddProduct(request.POST)

        if form.is_valid():
            title = form['title'].value()
            description = form['description'].value()

            product.title = title
            product.description = description
    
            product.save()
            
    return render(request, url, {"products":Product.objects.all(), "form":AddProduct()})

def trades(request):
    url = 'trades.html'
            
    return render(request, url, {"trades":Trade.objects.all(), "form":AddProduct()})

def press(request):
    url = 'press.html'

    return render(request, url)