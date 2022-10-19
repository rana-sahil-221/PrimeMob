# PrimeMob

PrimeMob is an exclusive online store for buying wide variety of Smartphones and Tablets. This E-Commerce website is developed in Python-Django.



## Built With



* Front End:- HTML, CSS, BootStrap
* Back End:- Python, Django Framework,SQLITE Database




## Getting Started




* Install django on system

```bash
  pip3 install django
```
* Creating Project
```
 django-admin startproject parentapp
 python manage.py runserver
```
* Starting the app inside parentapp
```
 python manage.py startapp baseapp
```

    
## Building Project
* Edit the urls.py file of parentapp to call it to baseapp urls.py
```
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('baseapp.urls')),
]
```
* Now make a urls.py file in baseapp and define function calls
```
from . import views
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('',views.register,name='register'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    #path('home/',views.home,name='home'),
]
```

* In views.py, write functions to define their functionality
```
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
    return render(request,'baseapp/register.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        reg_user = User.objects.create_user(username,email,pass1)
        reg_user.save()
        messages.success(request, "Your account has been successfully created!!")
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
```

* Now make a templates folder inside baseapp to store html templates