from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'school/index.html', context={'hello': "Hello World! "})

def url_test(request, test):
    return render(request, 'school/index.html', context={'hello': "Hello World! "+test})


def school_list(request):
    # schools = School.objects.all()
    schools = ['sc1', 'sc2', 'sc3']
    return render(request, 'school/school-list.html', {'schools':schools})