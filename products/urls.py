from django.urls import path

from products.views import product_detail, cat, main

urlpatterns = [
    path('', main, name='main'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('<int:pk>/', cat, name='cat'),
]
