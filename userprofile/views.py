from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserAdminCreationForm, BecomeVendorForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .models import *

from store.forms import ProductForm
from store.models import Product, Category, Order, OrderItem
get_object_or_404

from django.utils.text import slugify


def vendor_detail(request, vendor_name):
    #vendor_name = Vendor.objects.all()
    #vendor_name = str(vendor_name)
    products = Product.objects.filter(status=Product.ACTIVE)
    return render(request, 'vendor_detail.html', {
        'products': products,
        #'vendor_name': vendor_name,
    })

#@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            
            messages.success(request, f'{product.title} added Successfully ...')
            return redirect('my_store')
    else:
            form = ProductForm()            # form = ProductForm(), 'form' : form, {{ form.as_p }} three 3 line import default fields to add_product.html
    
    return render(request, 'add_product.html', {
        'form' : form,
    })

#@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Changes in product {product.title} was saved !')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {
        'product':product,  
        'form': form 
    })

#@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETEED
    product.save()

    messages.success(request, f'Product {product.title} was deleted !') 
    return redirect('my_store')

#@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETEED)
    order_items = OrderItem.objects.filter(product__user=request.user)
    order_items.total = sum(i.order.paid_amount for i in order_items)
    
    return render(request, 'my_store.html', {
        'products': products,
        'order_items': order_items,
        'order_items.total': order_items.total,
    })

#@login_required
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)  # pk matched with pk from url

    return render(request, 'my_store_order_detail.html', {
        'order': order
    })

#@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('myaccount')
        
        else:
            messages.info(request, 'Password or Username is incorrect')
            

    return render(request, 'login.html')


def signup(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')

            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('login')
    return render(request, 'signup.html', {'form': form})

def forgot(request):
    return render(request, 'forgot.html')


def become_vendor(request):
    form = BecomeVendorForm()
    if request.method == 'POST':
        form = BecomeVendorForm(request.POST)
        if form.is_valid():
            vendor_name = form.save()
            vendor_name = form.cleaned_data.get('vendor_name')

            messages.success(request, 'Added account of ' + str(vendor_name) + ' to vednor')
            return redirect('my-store')
        else:
            form = BecomeVendorForm()  
            print(form.errors)
            print("=== invlaid form ===")
    else:
        print("=== post error ===")
    return render(request, 'become_vendor.html', {'form': form})

