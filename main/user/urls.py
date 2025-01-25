from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_menu),
    path('account', views.account),
    path('shop', views.shop)
]
