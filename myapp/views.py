from django.shortcuts import render, HttpResponse , redirect
from myapp.models import Users
from myapp.models import Donation
from myapp.models import Order
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = User.objects.create_user(first_name = fname, last_name = lname, email = email,username = username, password = password)
        data.save()
        messages.success(request, 'User created successfully!')
        return redirect('login')
    return render(request,'signup.html')

def index(request):
    context = {
        "var": "This is sent"
    }
    return render(request,'home.html',context)
    #return HttpResponse("This is our home page")

def donate(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        door_number = request.POST.get('door_number')
        street = request.POST.get('street')
        area = request.POST.get('area')
        city = request.POST.get('city')
        food_type = request.POST.get('food_type')
        food_name = request.POST.get('food_name')
        quantity = request.POST.get('quantity')
        phone_number = request.POST.get('phone_number')

        donation = Donation(
            fname=fname,
            lname=lname,
            door_number=door_number,
            street=street,
            area=area,
            city=city,
            food_type=food_type,
            food_name=food_name,
            quantity=quantity,
            phone_number=phone_number
        )
        donation.save()
        messages.success(request, 'Donation submitted successfully!')
    return render(request, 'donate.html')

def order(request):
    donation_list = Donation.objects.all()  # Query all records from the User table
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        food_id = request.POST.get('food_id')
        door_number = request.POST.get('door_number')
        street = request.POST.get('street')
        area = request.POST.get('area')
        city = request.POST.get('city')
        quantity = request.POST.get('quantity')
        phone_number = request.POST.get('phone_number')

        orders = Order(
            fname=fname,
            lname=lname,
            food_id=food_id,
            door_number=door_number,
            street=street,
            area=area,
            city=city,
            quantity=quantity,
            phone_number=phone_number
        )
        orders.save()
        messages.success(request, 'Order placed successfully!')

    return render(request,'order.html', {'donations': donation_list})
    #return HttpResponse("This is our services page")

def deliver(request):
    # Fetch Donations details where food_id matches with the ID in Order table
    donations = Donation.objects.filter(id__in=Order.objects.values('food_id'))

    # Fetch order details corresponding to each donation
    order_details = {}
    for donation in donations:
        orders = Order.objects.filter(food_id=donation.id)
        order_details[donation.id] = [{'city':  order.city,'area': order.area, 'phone': order.phone_number,'quantity':order.quantity,'id':order.id} for order in orders]

    context = {
        'donations': donations,
        'order_details': order_details,
    }
    return render(request, 'deliver.html', context)

    #return HttpResponse("This is our contact page")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'User logged in successfully!')
            return redirect('donate')
        else :
            messages.error(request, 'Invalid credentials, Please try again!')
        
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

    

 
