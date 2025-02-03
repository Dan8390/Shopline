from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.show_user_menu, name="user_menu"),
    path('<int:user_id>/account', views.show_account, name="account"),
    path('<int:user_id>/producers', views.show_producers, name="producers"),
    path('<int:user_id>/shop', views.show_shop, name="shop"),
    path('<int:user_id>/history', views.show_history, name="history"),
    path('login/', views.show_login, name="login"),
    path('create', views.show_create, name="create")
]
