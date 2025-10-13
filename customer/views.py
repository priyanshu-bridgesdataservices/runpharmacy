from django.shortcuts import render

def login_signup(request):
    return render(request, 'customer/login_signup.html')

def dashboard(request):
    return render(request, 'customer/dashboard.html')

def prescription_upload(request):
    return render(request, 'customer/prescription_upload.html')

def quote_comparison(request):
    return render(request, 'customer/quote_comparison.html')

def checkout_order_confirmation(request):
    return render(request, 'customer/checkout_order_confirmation.html')

def order_tracking(request):
    return render(request, 'customer/order_tracking.html')

def my_orders(request):
    return render(request, 'customer/my_orders.html')

def profile(request):
    return render(request, 'customer/profile.html')