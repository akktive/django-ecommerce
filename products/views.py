import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import *
from .utils import cartData
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log-url')
    else:
        form = UserCreationForm()
    data = cartData(request)
    cartItems = data['cartItems']
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/register.html', context={
        'categories': categories,
        'products': products,
        'cartItems': cartItems,
        'form': form
    })


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mainpage-url')
    else:
        form = AuthenticationForm()
    data = cartData(request)
    cartItems = data['cartItems']
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/login.html', context={
        'categories': categories,
        'products': products,
        'cartItems': cartItems,
        'form': form
    })


def logoutPage(request):
    if request.method == 'POST':
        logout(request)
        return redirect('mainpage-url')


def category_page(request, category_name):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    categories = Category.objects.all()
    category_obj = get_object_or_404(Category, url=category_name)
    return render(request, 'products/category_page.html', context={
        'category_obj': category_obj,
        'categories': categories,
        'cartItems': cartItems,
        'products': products
    })


def main_page(request):
    data = cartData(request)
    cartItems = data['cartItems']
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/main_page.html', context={
        'categories': categories,
        'products': products,
        'cartItems': cartItems
    })


def cart_page(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    categories = Category.objects.all()
    return render(request, 'products/cart.html', context={
        'categories': categories,
        'items': items,
        'order': order,
        'cartItems': cartItems
    })


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId', productId)
    print('action', action)
    customer = request.user
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(user=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        total = order.get_cart_total

        if order.get_cart_items > 0:
            if total == order.get_cart_total:
                order.complete = True
            order.save()
    else:
        print('user is not auth...')
    return JsonResponse('Payment complete!', safe=False)
