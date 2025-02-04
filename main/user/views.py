from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Product
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.


def show_user_menu(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/user_menu.html', {'user': user})


def show_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/account.html', {'user': user})


def show_shop(request, user_id):
    user = get_object_or_404(User, id=user_id)
    all_products = Product.objects.all()
    products_to_show = []
    for i in all_products:
        if i.amount > 0:
            products_to_show.append(i)

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            product.amount -= 1
            if user.bought_products:
                user.bought_products += (', ' + product.title)
            else:
                user.bought_products = product.title
            product.save()
            user.save()
            return redirect('shop', user_id=user_id)
        except:
            return HttpResponse('<h1>Товар не знайдений</h1>', status=404)
    return render(request, 'user/shop.html', {'products': products_to_show, 'user_id': user_id})


def show_producers(request, user_id):
    return render(request, "user/producers.html")


def show_history(request, user_id):
    user = get_object_or_404(User, id=user_id)
    products_str = user.bought_products
    products = products_str.split(', ')
    return render(request, 'user/history.html', {'products': products, 'user_id': user_id})


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
