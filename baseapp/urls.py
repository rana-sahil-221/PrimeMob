from . import views
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('',views.register,name='register'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('contact/',views.contact,name='contact'),
    path('home/',views.home,name='home'),
    #path('home/',views.home,name='home'),
]