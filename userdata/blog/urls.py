from django import views
from django.urls import path
from blog import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.sign_in,name='signin'),
    path('admission/',views.user_admission,name='admission'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.sign_out,name='logout'),
]