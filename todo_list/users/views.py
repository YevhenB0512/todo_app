from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect(reverse('tasks:tasklist'))
    else:
        if request.user.is_authenticated:
            return redirect('tasks:tasklist')

        form = UserLoginForm()

    context = {
        'title': 'ToDo - Вход',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def registration_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            login(request, user)
            return redirect(reverse('tasks:tasklist'))

    else:
        if request.user.is_authenticated:
            return redirect('tasks:tasklist')
        form = UserRegistrationForm()
    context = {
        'title': 'ToDo - Регистрация',
        'form': form
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    return render(request, 'users/profile.html')


def logout_user(request):
    logout(request)
    return redirect(reverse('users:login'))
