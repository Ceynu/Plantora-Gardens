from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from datetime import timezone
from . models import customer
from . models import plantshop
from . models import product
from . models import cartitem
from . models import orders
from. models import newaddress 
import stripe


# Create your views here.
def index(request):
    return render(request,'index.html')

#registration customer and plantshop
def customer_registration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        contact_number=request.POST.get('contact_number')
        street_address=request.POST.get('street_address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        country=request.POST.get('country')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        exists=customer.objects.filter(email=email).exists()
        if exists:
            return render(request,'useralreadytaken.html')
        else:
            reg=customer.objects.create(name=name,gender=gender,contact_number=contact_number,street_address=street_address,city=city,state=state,zipcode=zipcode,country=country,email=email,password=password,image=fs)
            reg.save()
            return render(request,'index.html',{'msg':'user registered successfully'})
        
    return render(request,'customer_registration.html')


def plantshop_registration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        contact_number=request.POST.get('contact_number')
        street_address=request.POST.get('street_address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        country=request.POST.get('country')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        exists=plantshop.objects.filter(email=email).exists()
        if exists:
            return render(request,'useralreadytaken.html')
        else:
            reg=plantshop.objects.create(name=name,contact_number=contact_number,street_address=street_address,city=city,state=state,zipcode=zipcode,country=country,email=email,password=password,image=fs)
            reg.save()
            return render(request,'index.html',{'msg':'user registered successfully'})
        
    return render(request,'plantshop_registration.html')


#login
def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if customer.objects.filter(email=email,password=password).exists():
        cstmr_details=customer.objects.get(email=request.POST['email'],password=password)
        if cstmr_details.password==request.POST['password']:
            request.session['cid'] = cstmr_details.id
            request.session['cname'] = cstmr_details.name
            request.session['email'] = email
            request.session['customer'] = 'customer'
    
            return render(request,'index.html')
        
        
    elif plantshop.objects.filter(email=email,password=password).exists():
        ps_details=plantshop.objects.get(email=request.POST['email'],password=password)
        if ps_details.password==request.POST['password']:
            request.session['psid'] = ps_details.id
            request.session['psname'] = ps_details.name
            request.session['email'] = email
            request.session['plantshop'] = 'plantshop'
    
            return render(request,'index.html')
    else:
        return render(request,'login.html',{'status':'Invalid username or password'})


#logout    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'index.html')


#profile
def customer_profile(request):
    tem=request.session['cid']
    vpro=customer.objects.get(id=tem)
    return render(request,'customer_profile.html',{'result':vpro})

def plantshop_profile(request):
    tem=request.session['psid']
    vpro=plantshop.objects.get(id=tem)
    return render(request,'plantshop_profile.html',{'result':vpro})


#edit,update and delete - customer
def edit_customer_view(request):
    return render(request,'edit_customer_view.html')

def edit_customer(request,id):
    upt = customer.objects.get(id=id)
    return render(request,'edit_customer_view.html',{'result':upt})

def update_customer(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        contact_number=request.POST.get('contact_number')
        street_address=request.POST.get('street_address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        country=request.POST.get('country')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']    
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        reg=reg=customer.objects.create(name=name,gender=gender,contact_number=contact_number,street_address=street_address,city=city,state=state,zipcode=zipcode,country=country,email=email,password=password,image=fs)
        reg.save()
        return render(request,'index.html',{'msg':'Profile updated successfully'})
    
def delete_customer(request,id):
    member = customer.objects.get(id=id)
    member.delete()
    return redirect(index)


#edit update and delete plantshop
def edit_plantshop_view(request):
    return render(request,'edit_plantshop_view.html') #ith view chyyan maathram

def edit_plantshop(request,id):
    upt = plantshop.objects.get(id=id)
    return render(request,'edit_plantshop_view.html',{'result':upt}) #ith athilekk data pass chyyan

def update_plantshop(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        gender=request.get('gender')
        contact_number=request.POST.get('contact_number')
        street_address=request.POST.get('street_address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        country=request.POST.get('country')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        reg=plantshop.objects.create(name=name,gender=gender,contact_number=contact_number,street_address=street_address,city=city,state=state,zipcode=zipcode,country=country,email=email,password=password,image=fs)
        reg.save()
        return redirect('plantshop_profile')  # ith values update chyyan

    # Handle GET request to display form with current data
    return render(request, 'edit_plantshop_view.html', {'result': reg})

def delete_plantshop(request,id):
    member = plantshop.objects.get(id=id)
    member.delete()
    return redirect(index)


#product -add and delete
def add_product(request):
    tem=request.session['psid']
    reg=plantshop.objects.get(id=tem)
    return render(request,'add_product.html',{'res':reg})

def add_product_save(request):
    tem=request.session['psid']
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        description = request.POST.get('description')
        shop_instance = plantshop.objects.get(id=tem)
        image = request.FILES['image']
        f = FileSystemStorage()
        fs = f.save(image.name, image)
        regsave = product(product_name=product_name,price=price,category=category,description=description,shop_name=shop_instance,image=fs)
        regsave.save()
    return render(request,'added_successfully.html')

def added_successfully(request):
    return render(request,'added_successfully.html')

def delete_product(request):
    prdct = product.objects.get(id=id)
    prdct.delete()
    return redirect(add_product)


def product_list_view_for_customer(request):
    products = product.objects.all()  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)

def product_list_all(request):
    products = product.objects.all()  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)

def product_list_cacti(request):
    products = product.objects.filter(category='Cacti')  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)

def product_list_indoor(request):
    products = product.objects.filter(category='Indoor Plants')  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)

def product_list_flowering(request):
    products = product.objects.filter(category='Flowering Plants')  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)

def product_list_fruit(request):
    products = product.objects.filter(category='Fruit Plants')  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)

def product_list_hanging(request):
    products = product.objects.filter(category='Hanging Plants')  # Fetch all products
    context = {'product': products}
    return render(request, 'product_list_view_for_customer.html', context)


def my_products(request):
    tem=request.session['psid']
    plantshop_instance = plantshop.objects.get(id=tem)
    dict_product={
        'products':product.objects.filter(shop_name=plantshop_instance)
    }
    return render(request,'my_products.html',dict_product)



def product_profile(request,id):
    product_instance = product.objects.get(id=id)
    context = {'product': product_instance}
    return render(request,'product_profile.html',context)

def add_product_to_cart(request,id):
    tem = request.session['cid']
    if request.method=="POST":
        user_instance=customer.objects.get(id=tem)
        product_instance=product.objects.get(id=id)
        quantity=request.POST.get('quantity')
        reg = cartitem.objects.create(user=user_instance,product=product_instance,quantity=quantity)
        reg.save()
        return render(request,'added_to_cart_succesfully.html')
    
def cart_view(request):
    tem=request.session['cid']
    user_instance = customer.objects.get(id=tem)
    dict_cartitem={
        'cartitem':cartitem.objects.filter(user=user_instance)
    }
    return render(request,'cart_view.html',dict_cartitem)

def delete_cartitem(request,id):
    member = cartitem.objects.get(id=id)
    member.delete()
    return redirect(cart_view)


def proceed(request,id):
    tem = request.session['cid']
    if request.method == "POST":
        user_instance = customer.objects.get(id=tem)

        cart_item = cartitem.objects.get(id=id)
        quantity = request.POST.get('quantity')
        reg = orders.objects.create(user=user_instance, product=cart_item, quantity=quantity)
        reg.save()

        return redirect(reverse('order_summary', args=[id]))

    # Handle cases where the request method is not POST
    return redirect('cart_view')

def order_summary(request,id):
    tem=request.session['cid']
    user_instance = customer.objects.get(id=tem)
    
    cart_instance = cartitem.objects.get(id=id)
    context = {
        'user': user_instance,
        'plant': cart_instance,
    }
    return render(request,'order_summary.html',context)

def buy_now(request,id):
    tem=request.session['cid']
    if request.method=="POST":
        user_instance = customer.objects.get(id=tem)
        order_instance = cartitem.objects.get(id=id, user=user_instance)
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')
        reg  = newaddress(user=order_instance,street_address=street_address,city=city,state=state,zipcode=zipcode,country=country)
        reg.save()
    
    
        return redirect('order_summary', id=id)  # Redirect to the order summary page with the order id

    return redirect('order_summary', id=id)


def orders_got(request):
# Retrieve all new addresses (assuming these represent orders)
    result = newaddress.objects.all()
    
    # Save the data to the orders model
    for address in result:
        order = orders.objects.create(
            user=address.user.user,  # customer instance
            product=address.user,    # cartitem instance
            quantity=address.user.quantity,
            ordered_date=address.ordered_date
        )
        order.save()
    
    context = {
        'result': result
    }
    return render(request, 'orders_got.html', context)



def save_order_from_address(address_id):
    address = newaddress.objects.get(id=address_id)
    
    order = orders.objects.create(
        user=address.user.user,  # customer instance
        product=address.user,    # cartitem instance
        quantity=address.user.quantity,
        ordered_date=address.ordered_date
    )
    order.save()

def my_orders(request):
    tem = request.session['cid']
    user_instance = customer.objects.get(id=tem)

    shop_got = cartitem.objects.filter(user=user_instance)

    return render(request, 'my_orders.html', {'result': shop_got})
    # return redirect('my_orders', id=user_instance.id)


def payment_success(request):
    if request.method =='POST':
        paymenysuccess=stripe.Charge.success(
            amount=500,
            currency='inr',
            description = 'Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render('payment_success.html')
    
def search_products(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    if query:
        products = product.objects.filter(product_name__icontains=query)  # Filter products by the search query
    else:
        products = product.objects.all()  # Return all products if no search query is provided
    return render(request, 'product_list_view_for_customer.html', {'products': products})

    


