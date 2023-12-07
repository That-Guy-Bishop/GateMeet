from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if the user is already authenticated

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')   
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")

        user = authenticate(request, username=username, password=password)
        print(f"Authenticated User: {user}")

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/dashboard/')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error': "Unknown Account. Please try again."})
    
    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.last_name + " " + request.user.last_name})


def credit_view(request):
    return render(request, 'credit.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def GateMeet(request):
    return render(request, 'GateMeet.html', {'name' : request.user.first_name + " " + request.user.last_name})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')
