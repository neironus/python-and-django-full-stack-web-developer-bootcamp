from django.shortcuts import render
from .forms import UsersForm
from .models import UserModel
import os

# Create your views here.
def home(request):
    print(os.path.dirname(__file__))
    if request.path == '/home/':
        dest = 'Home'
    else:
        dest = 'Index'
    return render(request, 'AppTwo/index.html', context={'name': 'Django!', 'dest': dest})
    
def _help(request):
    return render(request, 'help.html')

def users(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            new_users = UserModel.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)
            return home(request)


    return render(request, 'AppTwo/users.html', {'form': form})