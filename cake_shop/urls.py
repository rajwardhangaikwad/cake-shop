"""
URL configuration for cake_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', views.home, name='home'),

    # AUTH SYSTEM
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),

    # CART
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),

    # REMOVE ITEM
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    # INCREASE / DECREASE QTY
    path('increase/<int:product_id>/', views.increase_qty, name='increase_qty'),
    path('decrease/<int:product_id>/', views.decrease_qty, name='decrease_qty'),

    # CHECKOUT
    path('checkout/', views.checkout, name='checkout'),

    # PLACE ORDER
    path('place-order/', views.place_order, name='place_order'),

    # ORDER HISTORY
    path('orders/', views.orders, name='orders'),

]

# MEDIA FILES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)