from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CustomerForm
from .models import Customer, Region, Province, City
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

# Create your views here.

#    form = CustomerForm(request.POST or None)
#    if form.is_valid():
#        user = request.user
#        form.save()
#    return render(request, 'cif/home.html', {'form':form})


class HomeView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer:customer')
    template_name = 'cif/home.html'


#@login_required(login_url='/login/')
# def home(request):
#     if request.method == 'GET':
#         form = Customer.objects.all()
#         return render(request, 'cif/home.html', {'form': form})
#     else:
#         try:
#             form = CustomerForm(request.POST, request.FILES)
#             newcustomer = form.save(commit=True)
#             newcustomer.created_by = request.user
#             newcustomer.image1 = request.FILES['image1']
#             newcustomer.image2 = request.FILES['image2']
#             newcustomer.save()
#             return redirect('customer:home')
#         except ValueError:
#             return render(request, 'cif/home.html', {'form':CustomerForm(), 'error':'Bad data passed in. Try again.'})

# Customer List
@login_required(login_url='/login/')
def customer(request):
    customerlist = Customer.objects.all()
    return render(request, 'cif/customerlist.html', {'obj':customerlist})

# CUstomer List View
@login_required(login_url='/login/')
def detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'cif/detail.html', {'customer':customer})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'cif/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'cif/login.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('customer:home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('customer:home')
