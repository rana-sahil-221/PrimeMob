from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from baseapp.models import Contact

def register(request):
    return render(request,'baseapp/register.html')

def home(request):
    return render(request,'baseapp/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        reg_user = User.objects.create_user(username,email,pass1)
        reg_user.save()
        messages.success(request, "Your account with username {} has been successfully created!!".format(username))
    return render(request,'baseapp/register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username,password = pass1)

        if user is not None:
            login(request,user)
            uname = user.username
            return render(request,'baseapp/home.html',{'fname':uname})
        else:
            messages.error(request,'Wrong Credentials')
    return render(request,'baseapp/register.html')

def signout(request):
    logout(request)
    #messages.success(request,"Logged out successfully!!")
    return redirect('signup')




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        contact =  Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request,'Form has been submitted Successfully!')
    return render(request,'baseapp/contact.html')
