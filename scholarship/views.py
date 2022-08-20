from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'home.html')


#----------------------------------------------------
#               ADMIN
#----------------------------------------------------

# admin login page here:
def admin_login(request):

    
    error=""

    if request.method == "POST":
        
        uName = request.POST['uname']
        pwd = request.POST['psw']

        ADMIN = authenticate(username=uName, password=pwd)

        try:
            if ADMIN.is_staff:
                login(request, ADMIN)
                error="no"
        
        except:
            error="yes"

    dict = {'Error': error}

    return render(request, 'admin_login.html', dict)

# Admin Home Page here:
def admin_home(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    return render(request, 'admin_home.html')

# View Users Page in admin_home:
def view_users(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    studentdata = StudentUser.objects.all()

    dic = {'userdata': studentdata}


    return render(request, 'view_users.html', dic)

# Delete User Page by admin:
def delete_user(request, pid):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    studentrecord = StudentUser.objects.get(id=pid)
    studentrecord.delete()

    return redirect('view_users')

# View Users Page in admin_home:
def providers_pending(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    providerdata = Provider.objects.filter(status="pending")

    dic = {'Providerdata': providerdata}

    return render(request, 'providers_pending.html', dic)

#----------------------------------------------------
#               SCHOLARSHIP PROVIDER
#----------------------------------------------------

# Privider sign-up here:
def provider_signup(request):

    error=""

    if request.method == "POST":

        fName = request.POST['fname']
        LName = request.POST['lname']
        comp = request.POST['company']
        phone = request.POST['contact']
        Email = request.POST['email']
        pwd = request.POST['psw']
        gen = request.POST['Radios']
        img = request.FILES['image']

        try:
            USER = User.objects.create_user(first_name=fName, last_name=LName, username=Email, password=pwd)
            Provider.objects.create(user=USER, mobile=phone, gender=gen, image=img, companyname=comp, usertype="provider", status="pending")
            error= "no"

        except:
            error= "yes"
    
    dic = {'Error': error}
    return render(request, 'provider_signup.html', dic)

# Privider Login here:
def provider_login(request):

    error=""

    if request.method == "POST":

        uName = request.POST['uname']
        pwd = request.POST['psw']

        PROVIDER = authenticate(username=uName, password=pwd)

        if PROVIDER:
            # error="no"
            try:
                providerdata = Provider.objects.get(user=PROVIDER)
                
                if providerdata.usertype == "provider" and providerdata.status != "pending":
                    login(request, PROVIDER)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
       
    dict = {'Error': error}

    return render(request, 'provider_login.html', dict) 

# Provider Home Page here:
def provider_home(request):

    if not request.user.is_authenticated:
        return redirect('provider_login')

    return render(request, 'provider_home.html')

#----------------------------------------------------
#               STUDENT USER
#----------------------------------------------------
# Student Signup here:
def user_signup(request):

    error=""

    if request.method == "POST":

        fName = request.POST['fname']
        LName = request.POST['lname']
        phone = request.POST['contact']
        Email = request.POST['email']
        pwd = request.POST['psw']
        gen = request.POST['Radios']
        img = request.FILES['image']

        try:
            USER = User.objects.create_user(first_name=fName, last_name=LName, username=Email, password=pwd)
            StudentUser.objects.create(user=USER, mobile=phone, gender=gen, image=img, usertype="student")
            error= "no"

        except:
            error= "yes"
    
    dic = {'Error': error}
    return render(request, 'user_signup.html', dic)


# Student Login here:
def user_login(request):

    error=""

    if request.method == "POST":

        uName = request.POST['uname']
        pwd = request.POST['psw']

        USER = authenticate(username=uName, password=pwd)

        if USER:
            # error="no"
            try:
                userdata = StudentUser.objects.get(user=USER)
                
                if userdata.usertype == "student":
                    login(request, USER)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
       
    dict = {'Error': error}

    return render(request, 'user_login.html', dict)

# Student Home Page here:
def user_home(request):

    if not request.user.is_authenticated:
        return redirect('user_login')

    return render(request, 'user_home.html')

#----------------------------------------------------
#          LOG OUT FUNCTION
#----------------------------------------------------

# Log-out Function Here:
def Logout(request):
    logout(request)
    return redirect('home')