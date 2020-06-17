from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "User logged")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid login or password")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['Name']
        last_name = request.POST['Surname']
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    messages.success(
                        request, "You are now registred. Please log in")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Logged out")
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
