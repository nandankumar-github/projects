from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from post.models import UserPost
# Create your views here.

def home(request):
    return render(request,'post/home.html')


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            print(username,password)
            user=authenticate(username=username,password=password)
            if user is not None:    
                login(request,user)
                return redirect('/dashboard/')
            else:
                messages.error(request,'username or password is incorrect')
        return render(request,'post/signin.html')
    else:
        return redirect('/dashboard/')

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            print(username,password)
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password).save()
            return redirect('/signin/')
        else:
            return render(request,'post/signup.html')
    else:
        return redirect('/dashboard/')



def user_post(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            name=request.POST['name']
            comment=request.POST['comment']
            user=request.user
            UserPost(who_post=user,name=name,comment=comment).save()
            return redirect('/dashboard/')
        else:
            return render(request,'post/post.html')
    else:
        return redirect('/dashboard/')




def dashboard(request):
    if request.user.is_authenticated:
        data=UserPost.objects.all().filter(who_post=request.user)    
        return render(request,'post/dashboard.html',{'data':data})
    else:
        return redirect('/signin/')



def sign_out(request):
    if request.user.is_authenticated:
        # if request.method=="POST":
            logout(request)
            return redirect('/signin/')
        # else:
        #     return HttpResponse('Bad request You have to login first')
    # else:
    #     return redirect('/signin/')
