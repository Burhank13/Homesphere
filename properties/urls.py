from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    # path('home', views.index, name='home'),
    path('register',views.register,name='register'),
    path('login',views.loginPage,name='login'),
]