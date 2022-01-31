from django.urls import path
from post import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signin/',views.sign_in,name='signin'),
    path('signout/',views.sign_out,name='signout'),
    path('signup/',views.sign_up,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('post/',views.user_post,name='post'),
]