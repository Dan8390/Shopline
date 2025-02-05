from django.shortcuts import render
from user.models import User, Product, Producer

# Create your views here.


def show_index(request):
    return render(request, "moderator/index.html")


def show_products(request):
    products = Product.objects.all()
    return render(request, "moderator/products.html", {'products': products})


def show_product_delete(request, product_id):
    return render(request, "moderator/product_delete.html", {'product_id': product_id})


def show_users(request):
    users = User.objects.all()
    return render(request, "moderator/users.html", {'users': users})


def show_user_delete(request, user_id):
    return render(request, "moderator/user_delete.html", {'user_id': user_id})


def show_producers(request):
    producers = Producer.objects.all()
    return render(request, "moderator/producers.html", {'producers': producers})


def show_producer_delete(request, producer_id):
    return render(request, "moderator/producer_delete.html", {'producer_id': producer_id})
