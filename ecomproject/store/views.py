from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'store/Store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items': items, 'order': order}
    return render(request, 'store/Cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items': items, 'order': order}
    return render(request, 'store/Checkout.html', context)


def updateItem(self):
    return JsonResponse("Item added", safe=False)