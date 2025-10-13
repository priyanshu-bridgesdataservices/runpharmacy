from django.urls import path

from . import views

app_name = 'pharmacy'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request-details/', views.request_details, name='request_details'),
    path('order-history/', views.order_history, name='order_history'),
    path('order-details/', views.order_details, name='order_details'),
    path('profile/', views.profile, name='profile'),
]
