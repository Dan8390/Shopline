from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField("Username", max_length=20)
    password = models.CharField("Пароль", max_length=30)
    name = models.CharField("Ім'я", max_length=20)
    surname = models.CharField("Прізвище", max_length=20)
    email = models.CharField("Електронна пошта", max_length=35)
    phone_number = models.CharField("Номер телефону", max_length=19)
    country = models.CharField("Країна", max_length=25)
    bought_products = models.TextField("Покупки", max_length=1500)

    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField("Назва", max_length=30)
    category = models.CharField("Категорія", max_length=30)
    price = models.IntegerField("Ціна")
    producer = models.CharField("Виробник", max_length=30)
    description = models.TextField("Опис", max_length=200)
    amount = models.IntegerField("Доступна кількість")

    def __str__(self):
        return self.title


class Producer(models.Model):
    title = models.CharField("Назва", max_length=30)
    country = models.CharField("Країна", max_length=30)
    products = models.TextField("Товари", max_length=120)
    description = models.TextField("Опис", max_length=500)
    site = models.TextField("Офіційний сайт", max_length=150)
    email = models.TextField("Електронна пошта", max_length=175)
    phone_numbers = models.TextField("Телефонні номери", max_length=120)

    def __str__(self):
        return self.title
