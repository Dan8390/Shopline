from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="show_index"),
    path('shop', views.show_shop, name="show_shop"),
    path('users', views.show_users, name="show_users")
]
