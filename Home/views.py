from django.shortcuts import render ,HttpResponse,redirect
from datetime import datetime
from .models import *
from superuser.models import *
from django.contrib import messages
from django.contrib.auth.models import *

# Create your views here.

def index(request):
    list = List.objects.all()
    list2= {
        'title': "Home",
        "list": list,
    }
    return render(request,'home/index.html', list2)

def dashboard(request):
    dashboard ={
        'title': "Admin",
    }
    if request.user.is_anonymous:
        return redirect(request,'home/login')
    return render(request,'superuser/index.html', dashboard)



def services(request):
    list = List.objects.all()
    list2= {
        'title': "Services",
        "list": list,
    }
    return render(request,'home/services.html', list2)

def about(request):
    list = List.objects.all()
    list2= {
        'title': "About",
        "list": list,
    }
    return render(request,'home/about.html', list2)

def contact(request):
    data ={
        'title': "Contact",
    }
    return render(request,'home/contact.html', data)

def saveContact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # image =request.FILES['image1']
        contact = Contact(name = name,email=email,phone =phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you for contacting us!')
    return redirect('home')


def bill(request):
    bill ={
        'title': "bill",
    }
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        ccname = request.POST.get('ccname')
        ccnumber = request.POST.get('ccnumber')
        ccexpiration = request.POST.get('ccexpiration')
        bill = Billing(firstName = firstName,lastName=lastName,username =username,email=email,address=address,address2=address2,ccname=ccname,ccnumber=ccnumber,ccexpiration=ccexpiration, date=datetime.today())
        bill.save()
        
    return render(request,'home/bill.html', bill)

def savebill(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        ccname = request.POST.get('ccname')
        ccnumber = request.POST.get('ccnumber')
        ccexpiration = request.POST.get('ccexpiration')
        bill = Billing(firstName = firstName,lastName=lastName,username =username,email=email,address=address,address2=address2,ccname=ccname,ccnumber=ccnumber,ccexpiration=ccexpiration, date=datetime.today())
        bill.save()
        messages.success(request, 'Have a safe Ride!')
    return redirect('home')

def signin(request):
    sign ={
        'title': "Sign in",
    }
    return render(request,'home/signup.html', sign)

def saveSignin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        uname = request.POST.get('uname')
        psw = request.POST.get('psw')
        signin = Signin(name = name,email=email,phone = phone,uname=uname,psw=psw, date=datetime.today())
        signin.save()
    return redirect('home')
    
def login(request):
    login ={
        'title': "login",
    }
    return render(request,'home/login.html',login)
        
def val_login(request):
    if request.method == "POST":
        uname=request.POST['uname']
        psw=request.POST['psw']
        try:
            if uname=='superuser' and psw=='superuser':
                request.session['uname']=uname
                return redirect('dashboard')
            cust=Signin.objects.filter(uname=uname,psw=psw,role=2).first()
            if cust:
                request.session['uname']=uname
                messages.add_message(request, messages.SUCCESS, "Login Successfully!!")
                return redirect('home')
            else:
                # return HttpResponse('wrong')
                messages.add_message(request, messages.ERROR, "Please enter correct username or password!!")
            return redirect('login')
        except:
            messages.add_message(request, messages.ERROR, "Something went wrong!!")
            return redirect('login')
    else:
        messages.add_message(request, messages.ERROR, "Wrong Request!!")
        return redirect('login')

def logout(request):
        del request.session['uname']
        messages.add_message(request, messages.SUCCESS, "Logout Successfully!!")
        return redirect('home')

def taxifare(request):
    list = List.objects.all()
    list2= {
        "list": list,
    }
    return render(request,'home/taxi-fare.html', list2)