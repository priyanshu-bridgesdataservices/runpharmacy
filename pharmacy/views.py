from django.shortcuts import render

def login(request):
    return render(request, 'pharmacy/login.html')

def dashboard(request):
    return render(request, 'pharmacy/dashboard.html')

def request_details(request):
    return render(request, 'pharmacy/request_details.html')

def order_history(request):
    return render(request, 'pharmacy/order_history.html')

def order_details(request):
    return render(request, 'pharmacy/order_details.html')

def profile(request):
    return render(request, 'pharmacy/profile.html')