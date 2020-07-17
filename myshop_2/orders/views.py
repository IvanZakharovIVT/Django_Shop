# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.person = request.user
            for item in cart:
                if item['quantity'] > item['product'].stock:
                    item['quantity'] = item['product'].stock
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                item['product'].stock -= item['quantity']
                if item['product'].stock == 0:
                    item['product'].available = False
                item['product'].save()
            # очистка корзины
            cart.clear()
            order.person = request.user
            order.save()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_list(request):
    if request.user.is_authenticated:
        pass
    this_user = request.user
    orders = this_user.order.all()
    items = orders[0].items.all()
    print ("so something")
    print ("id", orders[0].id)
    print ("items", items[0].product)
    print ("items", items[0].product.description)

    return render(request, 'orders/order/order_list.html',
                  {'orders': orders})

def order_items(request, id):
    order = get_object_or_404(Order,id=id)
    items = order.items.all()
    return render (request, 'orders/order/order_items.html',
            {'items': items})
