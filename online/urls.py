from django.urls import path
from .views import (
    index, products, 
    checkout, 
    cart, 
    order_category, 
    add_cart, 
    remove_cart, 
    change_quantity, 
    Product_Detail, 
    wishlist, 
    add_wishlist
    )

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('Product_Detail/<int:pk>/', Product_Detail.as_view(), name='Product_Detail'),

    path('order_category/', order_category, name='order_category'),
    path('add_cart/', add_cart, name='add_cart'),
    path('remove_cart/', remove_cart, name='remove_cart'),
    path('change_quantity/', change_quantity, name='change_quantity'),
    path('add_wishlist/', add_wishlist, name='add_wishlist'),
]