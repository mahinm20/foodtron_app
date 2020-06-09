from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth 
# Create your views here.

def home(request):
    return render(request,'foodtron_app/home.html')

def register(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                #If User already exist
                user = User.objects.get(username=request.POST['email'])
                return render(request,'account/register.html',{'error':'A user with the same email already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['email'],
                    first_name = request.POST['firstname'],
                    last_name = request.POST['lastname'],
                    email = request.POST['email'],
                    password = request.POST['password1']
                )
                auth.login(request,user)
                return redirect('register')
        else:
            return render(request,'account/register.html',{'error':'The password  does not match!'})
    else:
        return render(request,'account/register.html')                



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
        else:
            return render(request,'account/login.html',{'error':'username or password incorrect!'})
    else:
        return render(request,'account/login.html')