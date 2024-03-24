from django.shortcuts import render, redirect, HttpResponse

from .models import *
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.

def index(request):

    if request.method == "POST":
        product_id = request.POST.get('productid')
        remove = request.POST.get('remove')

        cart_id = request.session.get('cart')
        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1
            else:  
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id


    category_obj = Category.objects.all()
    category_id = request.GET.get("category_id")
    search = request.GET.get("search")

    if category_id:
        product_obj = Product.objects.filter(product_category=category_id)
    elif search:
        product_obj = Product.objects.filter(product_name__icontains = search)

    else:
        product_obj = Product.objects.all()

    context = {
        "category" : category_obj,
        "product" : product_obj
    }

    return render(request, 'home.html', context=context)

def signup(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        reg_obj = Registration(
            first_name = f_name,
            last_name = l_name,
            mobile = mobile,
            email = email,
            password = make_password(password),
            gender = gender

        )
        reg_obj.save()

    return redirect('home')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        email_id = Registration.objects.get(email=email)
        try:
            if check_password(password, email_id.password):
                request.session['name'] = email_id.first_name
                request.session['customer_id'] = email_id.id
                return redirect ('home')
            else:
                return HttpResponse("Wrong Password")
        except:
            return HttpResponse("Wrong Email, Please enter valid email")



def logout(request):
    request.session.clear()
    return redirect('home')


def cart_details(request):
    cart_id = list(request.session.get('cart').keys())

    product = Product.objects.filter(id__in = cart_id)

    context = {
        "product" : product
    }

    return render(request, 'cart.html', context=context)



def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return HttpResponse("Please login")

        cart_id = request.session.get('cart')

        product = Product.objects.filter(id__in = list(cart_id.keys()))
        
        for pro in product:
            order_obj = Order(
                address = address,
                mobile = mobile,
                customer = Registration(id=customer_id),
                price = pro.product_price,
                product = pro,
                quantity = cart_id.get(str(pro.id))

            )
            order_obj.save()
        return redirect('order')
    
def order_details(request):
    customer_id = request.session.get('customer_id')

    order = Order.objects.filter(customer=customer_id)
    tp = 0
    for i in order:
        tp = tp + (i.price * i.quantity)

    context = {
        "order": order,
        "tp": tp
    }
    return render(request, 'order.html', context=context)




from rest_framework import viewsets
from .serializers import RegistrationSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
