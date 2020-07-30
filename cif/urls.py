from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/', views.customer, name='customer'),

    path('customer/<int:customer_id>/', views.detail, name='detail'),

    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
