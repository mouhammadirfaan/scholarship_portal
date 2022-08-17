from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def provider_login(request):
    return render(request, 'provider_login.html')

def user_login(request):
    return render(request, 'user_login.html')

def user_signup(request):
    return render(request, 'user_signup.html')