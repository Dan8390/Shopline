from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="show_index"),
    path('products/', views.show_products, name="show_products"),
    path('products/<int:product_id>/detail', views.show_product_detail, name="product_detail"),
    path('products/<int:pk>/delete', views.ProductDeleteView.as_view(), name="product_delete"),
    path('save_products_to_file', views.save_products_to_file, name="save_products_to_file"),
    path('load_products_from_file', views.load_products_from_file, name="load_products_from_file"),
    path('users/', views.show_users, name="show_users"),
    path('users/<int:user_id>/detail', views.show_user_detail, name="user_detail"),
    path('users/<int:pk>/delete', views.UserDeleteView.as_view(), name="user_delete"),
    path('save_users_to_file', views.save_users_to_file, name="save_users_to_file"),
    path('load_users_from_file', views.load_users_from_file, name="load_users_from_file"),
    path('producers/', views.show_producers, name="show_producers"),
    path('producers/<int:producer_id>/detail', views.show_producer_detail, name="producer_detail"),
    path('producers/<int:pk>/delete', views.ProducerDeleteView.as_view(), name="producer_delete"),
    path('save_producers_to_file', views.save_producers_to_file, name="save_producers_to_file"),
    path('load_producers_from_file', views.load_producers_from_file, name="load_producers_from_file")
]
