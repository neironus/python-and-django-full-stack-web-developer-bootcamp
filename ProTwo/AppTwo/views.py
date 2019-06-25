from django.shortcuts import render
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