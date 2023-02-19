import json
import stripe
import uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from .cart import Cart
from .forms import OrderForm, MessageSellerForm
from .models import Product, Category, Order, OrderItem, Vendor
from core.forms import ContactForm

def add_to_cart(request, product_id):
    cart = Cart(request)
    print(product_id)
    cart.add(product_id)

    return redirect('cart_view')

def success(request):
    return render(request, 'success.html')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart_view.html', {
        'cart': cart
    })

#@login_required
def checkout(request):
    cart = Cart(request)

    if cart.get_total_cost() == 0:
        return redirect('cart_view')

    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        mobile = data['mobile']
        address = data['address']

        if first_name and last_name and email and mobile and address:
            form = OrderForm(request.POST)

            total_price = 0
            items = []

            for item in cart:
                product = item['product']
                total_price += product.discount_price

            items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.title
                    },
                    'unit_amount': product.discount_price
                },
                # 'quantity': item['quantity']
            })

            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types = ['card'],
                line_items = items,
                mode = 'payment',
                sucess_url = f'{settings.WEBSITE_URL}cart/checkout/success/',
                cancel_url = f'{settings.WEBSITE_URL}cart/',
        )
        payment_intent = session.payment_intent 

        order = Order.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            mobile = mobile,
            address = address,
            paid_amount = total_price,
            is_paid = True,
            order_id = uuid.uuid4(),
            created_by = request.user
        )

        for item in cart:
            product = item['product']
            price += product.discount_price
            item = OrderItem.objects.create(order=order, product=product,price=total_price)
        cart.clear()

        return JsonResponse({'session': session, 'order': payment_intent})
        # return redirect('myaccount') on success
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {
        'cart': cart,
        'form': form,
        'pub_key': settings.STRIPE_PUB_KEY,
    })


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {
        'query': query,
        'products': products,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    vendors = Vendor.objects.filter(status=Product.ACTIVE)[0:6]
    return render(request, 'category_detail.html', { 
        'category': category,
        'products': products,  #refers to related name in models.py of store
        'vendors': vendors,
         })

def product_detail(request, category_slug, slug):
    #category = get_object_or_404(Category, slug=slug)
    productss = Product.objects.all()
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    simliar = Product.objects.filter(status=Product.ACTIVE)[0:4]
    
    if request.method == 'POST':
        form = MessageSellerForm(request.POST)
        if form.is_valid():
            # modify subject field by pass the service instance to the form using the instance parameter
            form.instance.msg_subject = "Query about service %s" % product.title
            form.save()
            messages.success(request, "Success")
            form = MessageSellerForm()
        else:
            messages.error(request, "Failed")
    else:
        form = MessageSellerForm()
    

    return render(request, 'product_detail.html', {
        #'category': category,
        'product': product,
        'simliar': simliar,
        'form': form,
        'productss': productss,
    })