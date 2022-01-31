from audioop import add
from email import message
import re
import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import AdmissionModel

# Create your views here.

def home(request):
    return render(request,'blog/home.html')


def sign_up(request):
    if  not request.user.is_authenticated:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
            messages.success(request,'signup successfully')
            return redirect('/signin/')
        return render(request,'blog/signup.html')
    else:
        return redirect("/dashboard/")


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.error(request,'login successfully')
                return redirect('/dashboard/')
            else:
                messages.error(request,'username or password is incorrect')
        return render(request,'blog/sign.html')
    else:
        return redirect('/dashboard/')


def user_admission(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            name=request.POST['name']
            roll=request.POST['roll']
            address=request.POST['address']
            user=request.user
            AdmissionModel(admission_though=user,name=name,roll=roll,address=address).save()
            messages.success(request,'Admission Successfully')

            return redirect('/dashboard/')

        return render(request,'blog/admission.html')
    else:
        return redirect('/signin/')


def dashboard(request):
    if request.user.is_authenticated:
        data=AdmissionModel.objects.all().filter(admission_though=request.user)
        return render(request,'blog/dashboard.html',{'data':data})
    else:
        return redirect('/signin/')


def sign_out(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            logout(request)
            return redirect('/signin/')
        else:
            return HttpResponse('Bad request 404 error')

