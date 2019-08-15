from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, UserProfileForm

# Create your views here.
def home(request):
    # if request.user.is_authenticated:
    #     print(request.user)
    # else:
    #     print(None)
    # print(dir(request.user))
    # print('*' * 5)
    # print(request.META.get('HTTP_X_REAL_IP') or request.META.get('REMOTE_ADDR'))
    # print('*' * 5)
    context = {'user': request.user}
    return render(request, 'basic_app/index.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("basic_app:home"))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("basic_app:home"))
        return render(request, 'basic_app/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("basic_app:home"))
    
def sign_up(request):
    """
    * Создание пользователя +
    * Переадресация пользователя на страничу входа
    """
    if request.method == 'POST':
        # username = request.POST.get('username')
        # print(username)
        # password = request.POST.get('password')
        # email = request.POST.get('email')
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            print('*****************')
            print(user_form.cleaned_data['username'])
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_profile.save(commit=False)
            profile.user = user
            profile.save()
            print('*****************')
            return HttpResponseRedirect(reverse("basic_app:login-user"))
        
        '''
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
        '''
        # print(user)
        # UserForm = UserForm()
        # return render(request, 'basic_app/signup.html',
        #         {
        #             'user_form': UserForm,
        #             'user_profile': UserProfileForm
        #         }
        #     )
    # UserForm = UserForm()
    return render(request, 'basic_app/signup.html',
                {
                    'user_form': UserForm,
                    'user_profile': UserProfileForm
                }
            )