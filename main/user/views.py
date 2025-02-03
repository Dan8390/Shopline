from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Product
from .forms import UserForm

# Create your views here.


def show_user_menu(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/user_menu.html', {'user': user})


def show_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/account.html', {'user': user})


def show_shop(request, user_id):
    products = Product.objects.all()
    return render(request, 'user/shop.html', {'products': products})


def show_producers(request, user_id):
    return render(request, "user/producers.html")


def show_history(request, user_id):
    return render(request, 'user/history.html')


def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('user_menu', user_id=user.id)
        except:
            return render(request, 'user/login.html')

    return render(request, 'user/login.html')


def show_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.bought_products = ""
            user.save()
            return redirect('login')

    form = UserForm()
    data = {'form': form}
    return render(request, 'user/create.html', data)
