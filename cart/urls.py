from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_dec/<int:product_id>/',views.min_cart,name='cart_dec'),
    path('delete/<int:product_id>/',views.cart_delete,name='delete'),
]