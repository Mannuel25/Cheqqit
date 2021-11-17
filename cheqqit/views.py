from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'signup.html', context)

def signinPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('webapp')
            else:
                messages.error(request, "Invalid username or password")
        context = {}
        return render(request, 'registration/login.html', context)

def signoutUser(request):
    logout(request)
    return redirect('home')
