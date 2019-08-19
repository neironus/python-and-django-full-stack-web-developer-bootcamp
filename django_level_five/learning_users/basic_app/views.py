from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, UserProfileForm

# Create your views here.
def home(request):
    print(request.user)
    context = {'user': request.user}
    return render(request, 'basic_app/index.html', context)

def login_user(request):
    # print(request.GET.get('key'))
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # print(request.POST)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("basic_app:home"))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("basic_app:home"))
        return render(request, 'basic_app/login.html')

@login_required(login_url='/basic-app/login')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("basic_app:home"))
    
def sign_up(request):
    registered = False
    """
    * Переадресация пользователя на страничу входа
    """
    if request.method == 'POST':
        # print(request.FILES)
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            print(user_profile.cleaned_data['profile_pic'])
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_profile.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            # print('*****************')
            return HttpResponseRedirect(reverse("basic_app:login-user"))
    return render(request, 'basic_app/signup.html',
                {
                    'user_form': UserForm,
                    'user_profile': UserProfileForm
                }
            )

def profile_user(request, user_name):
    # user_name=request.user
    # print('*****************')
    # print(user_name)
    user = get_object_or_404(User, username=user_name)
    # print('*****************')

    # user = User.objects.get(username)
    return render(request, 'basic_app/user-profile.html', {'user':user})