from django.shortcuts import render

# Create your views here.


def show_index(request):
    return render(request, "moderator/index.html")


def show_shop(request):
    return render(request, "moderator/products.html")


def show_users(request):
    return render(request, "moderator/users.html")
