from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_user_menu, name="user_menu"),
    path('account', views.show_account, name="account"),
    path('shop', views.show_shop, name="shop"),
    path('history', views.show_history, name="history")
]
