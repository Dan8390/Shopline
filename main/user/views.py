from django.shortcuts import render

# Create your views here.


def show_user_menu(request):
    return render(request, 'user/user_menu.html')


def show_account(request):
    return render(request, 'user/account.html')


def show_shop(request):
    return render(request, 'user/shop.html')


def show_history(request):
    return render(request, 'user/history.html')
