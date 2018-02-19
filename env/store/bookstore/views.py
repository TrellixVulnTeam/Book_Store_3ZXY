#from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth import views as auth_view
#from django.contrib.auth.views import login,logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth.views import login
# Create your views here.

def home(request):
    return render(request, "home.html")

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/login/modelforms/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})
