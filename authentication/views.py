from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        last_name = request.POST.get("lname")
        first_name = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        cnfrm_password = request.POST.get("pass2")

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = first_name
        myuser.last_name = last_name


        myuser.save()

        messages.success(request,"Your account has been sucessfully created")
        return redirect('signin')

    return render(request,'authentication/index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print("yes")
            messages.success(request,"Sucessfully logged in")
            return render(request,'authentication/dashboard.html',{'fname':username})
        else:
            messages.error(request,"OPPS! Wrong Credentials")
            print("wrong")
            return redirect('home')

    return render(request,'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Sucessfully logged out")
    return redirect('home')

def signup_page(request):
    return render(request,'authentication/signup.html')