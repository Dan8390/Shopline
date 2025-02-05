from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="show_index"),
    path('products', views.show_products, name="show_products"),
    path('product_delete/<int:product_id>', views.show_product_delete, name="product_delete"),
    path('users', views.show_users, name="show_users"),
    path('user_delete/<int:user_id>', views.show_user_delete, name="user_delete"),
    path('producers', views.show_producers, name="show_producers"),
    path('producer_delete/<int:producer_id>', views.show_producer_delete, name="producer_delete")
]
