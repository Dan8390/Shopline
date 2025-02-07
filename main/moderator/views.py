import json
from django.shortcuts import render, get_object_or_404
from user.models import User, Product, Producer
from django.views.generic import DeleteView
from django.http import HttpResponse

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


def save_products_to_file(request):
    products = Product.objects.all()

    products_data = {
        'products': [{
            'title': product.title,
            'category': product.category,
            'price': product.price,
            'producer': product.producer,
            'description': product.description,
            'amount': product.amount
        } for product in products]
    }

    with open('products.json', 'w') as file:
        json.dump(products_data, file, indent=4)
    return render(request, 'moderator/save_products_to_file.html')


def load_products_from_file(request):
    try:
        with open('products.json', 'r') as file:
            products_data = json.load(file)
            for product in products_data.get('products'):
                Product.objects.get_or_create(title=product['title'], category=product['category'],
                                              price=product['price'], producer=product['producer'],
                                              description=product['description'], amount=product['amount'])
            return render(request, "moderator/load_products_from_file.html")
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка імпорту файлу. Файл не знайдено</4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка імпорту файлу. JSON не може розшифруватися</4>')


def show_users(request):
    users = User.objects.all()
    return render(request, "moderator/users.html", {'users': users})


def show_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "moderator/user_detail_view.html", {'user': user})


def save_users_to_file(request):
    users = User.objects.all()

    users_data = {
        'users': [{
            'username': user.username,
            'password': user.password,
            'name': user.name,
            'surname': user.surname,
            'email': user.email,
            'phone_number': user.phone_number,
            'country': user.country,
            'bought_products': user.bought_products
        } for user in users]
    }

    with open('users.json', 'w') as file:
        json.dump(users_data, file, indent=4)
    return render(request, 'moderator/save_users_to_file.html')


def load_users_from_file(request):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
            for user in users_data.get('users'):
                User.objects.get_or_create(username=user['username'], password=user['password'], name=user['name'],
                                           surname=user['surname'], email=user['email'],
                                           phone_number=user['phone_number'], country=user['country'],
                                           bought_products=user['bought_products'])
            return render(request, "moderator/load_users_from_file.html")
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка імпорту файлу. Файл не знайдено</4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка імпорту файлу. JSON не може розшифруватися</4>')


def show_producers(request):
    producers = Producer.objects.all()
    return render(request, "moderator/producers.html", {'producers': producers})


def show_producer_detail(request, producer_id):
    producer = get_object_or_404(Producer, id=producer_id)
    return render(request, "moderator/producer_detail_view.html", {'producer': producer})


def save_producers_to_file(request):
    producers = Producer.objects.all()

    producers_data = {
        'producers': [{
            'title': producer.title,
            'country': producer.country,
            'products': producer.products,
            'description': producer.description,
            'site': producer.site,
            'email': producer.email,
            'phone_numbers': producer.phone_numbers
        } for producer in producers]
    }

    with open('producers.json', 'w') as file:
        json.dump(producers_data, file, indent=4)
    return render(request, 'moderator/save_producers_to_file.html')


def load_producers_from_file(request):
    try:
        with open('producers.json', 'r') as file:
            producers_data = json.load(file)
            for producer in producers_data.get('producers'):
                Producer.objects.get_or_create(title=producer['title'], country=producer['country'],
                                               products=producer['products'], description=producer['description'],
                                               site=producer['site'], email=producer['email'],
                                               phone_numbers=producer['phone_numbers'])
            return render(request, "moderator/load_producers_from_file.html")
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка імпорту файлу. Файл не знайдено</4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка імпорту файлу. JSON не може розшифруватися</4>')
