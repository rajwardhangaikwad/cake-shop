from django.urls import path
from . import views

urlpatterns = [

    
    path('', views.home, name='home'),

    path('cakes/', views.cakes, name='cakes'),

    path('pastries/', views.pastries, name='pastries'),

    path('signup/', views.signup, name='signup'),

    
    path('cart/', views.cart, name='cart'),

    
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    
    path('increase/<int:product_id>/', views.increase_qty, name='increase_qty'),


    path('decrease/<int:product_id>/', views.decrease_qty, name='decrease_qty'),

    
    path('checkout/', views.checkout, name='checkout'),

    
    path('place-order/', views.place_order, name='place_order'),

    
    path('orders/', views.orders, name='orders'),

]