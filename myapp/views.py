from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import MyLoginForm, MyRegisterForm


def home(request):
    return render(request, 'home.html')


def mylogin(request):
    if request.method == 'POST':
        form = MyLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = MyLoginForm()
    return render(request, 'login.html', {'form': form})

def myregister(request):
    if request.method == 'POST':
        form = MyRegisterForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('home')
    else:
        form = MyRegisterForm()
    return render(request, 'register.html', {'form': form})


def mylogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')