# from registerApp.decorators import unauthenticated_user
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreateNewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user

@unauthenticated_user
def register_view(request):
    form = CreateNewUserForm()
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created Successfully')
            return redirect('login')
    context = {'form':form}
    return render(request,'registerApp/register.html',context)


@unauthenticated_user
def login_view(request):
    if request.method =='POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        user = authenticate(request,username=userName,password=passWord)
        if user is not None:
            login(request,user)
            return redirect('index')  # as soon as login redirect to index page
        else:
            messages.info(request,'Incorrect UserName or Password')

    return render(request,'registerApp/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')