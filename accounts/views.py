from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid login credentials.')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logout')
        return redirect('home')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exist!')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist!')
                return redirect('register')
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            user.save()
            auth.login(request, user)
            messages.success(request, 'You are registered successfully and logged in.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
