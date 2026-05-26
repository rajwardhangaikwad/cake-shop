from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



def home(request):

    query = request.GET.get('q')
    category = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    return render(request, 'home.html', {
        'products': products,
        'query': query,
        'category': category
    })



def signup(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form
    })



def add_to_cart(request, product_id):

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1

    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart

    return redirect('home')



def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect('cart')



def increase_qty(request, product_id):

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1

    request.session['cart'] = cart

    return redirect('cart')



def decrease_qty(request, product_id):

    cart = request.session.get('cart', {})

    if str(product_id) in cart:

        cart[str(product_id)] -= 1

        if cart[str(product_id)] <= 0:
            del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect('cart')



def cart(request):

    cart = request.session.get('cart', {})

    products = []

    total = 0

    for id, qty in cart.items():

        product = Product.objects.get(id=id)

        product.qty = qty

        product.total_price = product.price * qty

        total += product.total_price

        products.append(product)

    return render(request, 'cart.html', {
        'products': products,
        'total': total
    })



@login_required
def checkout(request):

    cart = request.session.get('cart', {})

    products = []

    total = 0

    for id, qty in cart.items():

        product = Product.objects.get(id=id)

        product.qty = qty

        product.total_price = product.price * qty

        total += product.total_price

        products.append(product)

    return render(request, 'checkout.html', {
        'products': products,
        'total': total
    })


@login_required
def place_order(request):

    cart = request.session.get('cart', {})

    if request.method == "POST":

        address = request.POST.get('address')

        total = 0

        
        order = Order.objects.create(
            user=request.user,
            total_price=0,
            address=address
        )

        
        for id, qty in cart.items():

            product = Product.objects.get(id=id)

            OrderItem.objects.create(
                order=order,
                product_name=product.name,
                price=product.price,
                quantity=qty
            )

            total += product.price * qty

        
        order.total_price = total
        order.save()

        
        request.session['cart'] = {}

        
        return render(request, 'success.html', {
            'order': order
        })

    return redirect('checkout')


@login_required
def orders(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, 'orders.html', {
        'orders': orders
    })