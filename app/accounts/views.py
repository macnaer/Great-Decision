from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("User logged!")
            return redirect("dashboard")
        else:
            print("Invalid login or password")
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
                print("User exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print("Email exists")
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
                    print("You are now registred. Please log in")
                    return redirect('login')
        else:
            print("Passwords do not match")
            return redirect('register')
    return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("Logged out")
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
