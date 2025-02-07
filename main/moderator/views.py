from django.shortcuts import render, get_object_or_404
from user.models import User, Product, Producer
from django.views.generic import DeleteView

# Create your views here.


class UserDeleteView(DeleteView):
    model = User
    success_url = '..'
    template_name = 'moderator/user_delete.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '..'
    template_name = 'moderator/product_delete.html'


class ProducerDeleteView(DeleteView):
    model = Producer
    success_url = '..'
    template_name = 'moderator/producer_delete.html'


def show_index(request):
    return render(request, "moderator/index.html")


def show_products(request):
    products = Product.objects.all()
    return render(request, "moderator/products.html", {'products': products})


def show_product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "moderator/product_detail_view.html", {'product': product})


def show_users(request):
    users = User.objects.all()
    return render(request, "moderator/users.html", {'users': users})


def show_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "moderator/user_detail_view.html", {'user': user})


def show_producers(request):
    producers = Producer.objects.all()
    return render(request, "moderator/producers.html", {'producers': producers})


def show_producer_detail(request, producer_id):
    producer = get_object_or_404(Producer, id=producer_id)
    return render(request, "moderator/producer_detail_view.html", {'producer': producer})
