from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import json
import datetime
from .models import *

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def index(request):
    return render(request, 'store/index.html')
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping':False}
        cartItems =order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping':False}
        cartItems =order['get_cart_items']
    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items 
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping':False}
        cartItems =order['get_cart_items']
    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
 
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,create = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem,create = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == float(order.get_cart_total):
            order.complete = True
            order.save()
            
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                Phone=data['shipping']['Phone'],
                home=data['shipping']['home'],
                size=data['shipping']['size'],
            )    
    else:
        {
            print('user is not logged in....')
        }    
    return JsonResponse('paymeat is completed', safe=False)



def loginpage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
           messages.info(request, "username or password is incorrect")
    context ={}
    return render(request, 'store/login.html', context)

def signuppage(request):
    
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confim password are not match!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request, "account was created successfully!")
            return redirect('loginpage')
    context ={}
    return render(request, 'store/signup.html', context)


def logoutPage(request):
    logout(request)
    return redirect('loginpage')





    





