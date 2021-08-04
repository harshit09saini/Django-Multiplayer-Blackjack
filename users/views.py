from django.shortcuts import render, redirect
from .forms import Login, Register
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form_data = form.cleaned_data
            username = form_data["username"]
            password = form_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('lobby')
            else:
                messages.info(request, "Invalid Credentials. Please Try Again")
                return redirect('login')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = Login()
    return render(request, "auth/login.html", {'form': form})


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form_data = form.cleaned_data
            username = form_data["username"]
            email = form_data["email"]
            password = form_data["password"]
            print(username, email, password)
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                auth.login(request, user)
                return redirect('lobby')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = Register()

    return render(request, "auth/register.html", {'form': form})

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("home")
