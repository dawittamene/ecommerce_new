from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('signuppage/', views.signuppage, name="signuppage"),
    path('logoutPage/', views.logoutPage, name="logoutPage"),

    
    
    
    
    
]