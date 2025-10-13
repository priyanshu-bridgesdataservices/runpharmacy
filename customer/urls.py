from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('login-signup/', views.login_signup, name='login_signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('prescription-upload/', views.prescription_upload, name='prescription_upload'),
    path('quote-comparison/', views.quote_comparison, name='quote_comparison'),
    path('checkout-order-confirmation/', views.checkout_order_confirmation, name='checkout_order_confirmation'),
    path('order-tracking/', views.order_tracking, name='order_tracking'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('profile/', views.profile, name='profile'),
]