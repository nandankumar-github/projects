from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from school.froms import StudentForm,Profile
from school.models import StudentModel
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def user_login(request):
    
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        print(fm.is_valid())

        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            print(username,password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'you have successfully login')
                return HttpResponseRedirect("/details/")
    else:
        fm=AuthenticationForm()
        
    
    return render(request,'school/login.html',{'form':fm})

def user_signup(request):
    fm=Profile()
    if request.method=='POST':
        fm=Profile(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Signup successfully')
            return redirect('/login/')

    return render(request,'school/signup.html',{'form':fm})



def user_logout(request):
    logout(request)
    return redirect('/login/')




def student_create(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request,'Data has been successfully created')
            return redirect('/details/')
    else:
        fm=StudentForm()

    return render(request,'school/student_create.html',{'form':fm})
    



def student_details(request):
    stud=StudentModel.objects.all()
    return render(request,'school/student_details.html',{'stud':stud})



def student_update(request,id):
    if request.method=="POST":
        stud=StudentModel.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=stud)
        if fm.is_valid():
            fm.save()

    else:
        stud=StudentModel.objects.get(pk=id)
        fm=StudentForm(instance=stud)
    return render(request,'school/student_update.html',{'form':fm})


def student_delete(request,id):
    stud=StudentModel.objects.get(pk=id)
    stud.delete()
    return HttpResponseRedirect('/details/')