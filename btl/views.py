from django.shortcuts import render


def index(request):
    return render(request, "btl/index.html")


def shopcart(request):
    return render(request, "btl/shop-cart.html")

def checkout(request):
    return render(request,"btl/checkout.html")
