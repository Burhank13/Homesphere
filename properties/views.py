from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import *
# Create your views here.
def register(request):
    form  = RegisterForm()
    context = {'form': form}
        
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)
    return render(request, 'register.html', context)
    

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request,user)
            print("Logged In")
            return redirect('register')
        else:
          messages.info(request, 'Incorrect username OR password')
    context = {}
    return render(request,'login.html')
