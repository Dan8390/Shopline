from django.shortcuts import render

# Create your views here.


def user_menu(request):
    return render(request, 'user/user_menu.html')


def account(request):
    return render(request, 'user/account.html')


def shop(request):
    return render(request, 'user/shop.html')
