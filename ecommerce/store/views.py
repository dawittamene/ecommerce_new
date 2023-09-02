from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *



# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        
    context = {'items':items, 'order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        
    context = {'items':items, 'order': order}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    
    print('Action:', action)
    print('productId:', productID)
    
    customer = request.user.customer
    product = product.objects.get(id=productID)
    order,create = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem,create = OrderItem.objects.get_or_create(order=order, complete=False)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()    
            
    
    
    
    
    return JsonResponse('it was update', safe=False)