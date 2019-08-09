from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, UserProfileForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print(request.user)
    else:
        print(None)
    # print('*' * 5)
    # print(request.META.get('HTTP_X_REAL_IP') or request.META.get('REMOTE_ADDR'))
    # print('*' * 5)
    return render(request, 'basic_app/index.html')

def login_user(request):
    # if request.user.is_authenticated:
    #     print(request.user)
    #     print(request)
    # else:
    #     print(None)
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Hello {login}")
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("basic_app:home"))
    return render(request, 'basic_app/login.html')
    
def sign_up(request):
    return render(request, 'basic_app/signup.html',
            {
                'user_form': UserForm,
                'user_profile': UserProfileForm
            }
        )