from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from school.models import CityModel, SchoolModel, StudentModel
from school.forms import CityForm, SchoolForm
# Create your views here.
def index(request):
    return render(request, 'school/index.html', context={'hello': "Hello World! "})

def url_test(request, test):
    return render(request, 'school/index.html', context={'hello': "Hello World! "+test})


def school_list(request):
    schools = SchoolModel.objects.all()
    # schools = ['sc1', 'sc2', 'sc3']
    return render(request, 'school/school-list.html', {'schools':schools})

def school_description(request, pk):
    print(request.GET)
    school = SchoolModel.objects.get(pk=pk)
    students = school.students.all()
    return render(request, 'school/school-description.html', {'school':school, 'students':students})

def school_edit(request, pk):

    school = SchoolModel.objects.get(pk=pk)
    form = SchoolForm(instance=school) # или чере словарь initial={'name': 'Secondary school №234', 'slug': 'secondary_school_234'}
    # можно не делать запрос к базе и забрать с урла все?
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            school.name = data.get('name')
            school.save()
    return render(request, 'school/school-edit.html', {'form':form})