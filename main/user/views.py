from django.shortcuts import render
from .models import Product

# Create your views here.


def show_user_menu(request):
    return render(request, 'user/user_menu.html')


def show_account(request):
    return render(request, 'user/account.html')


def show_shop(request):
    products = Product.objects.all()
    return render(request, 'user/shop.html', {'products': products})


def show_producers(request):
    return render(request, "user/producers.html")


def show_history(request):
    return render(request, 'user/history.html')
