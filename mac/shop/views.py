from django.shortcuts import render
from . models import Product
from math import ceil

from django.http import HttpResponse

# Create your views here.
def index (request):
    #products= Product.objects.all()
    #print(products)
    #n = len(products)
    #nslides = n//4 + ceil((n/4))-(n//4)

    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4)) - (n // 4)
        allprods.append([prod, range(1,nslides), nslides])

     # params = {'no_of_slides':nslides, 'range':range(1,nslides), 'product': products}
    #allprods = [[products, range(1, nslides), nslides] ,[products, range(1, nslides), nslides]]
    params = {'allprods':allprods}
    return render(request,'shop/index.html'  , params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact page")

def tracker(request):
    return HttpResponse("We are at Tracker page")

def search(request):
    return HttpResponse("We are at search page")

def productView(request):
    return HttpResponse("We are at product view  page")

def checkout(request):
    return HttpResponse("We are at checkout page")