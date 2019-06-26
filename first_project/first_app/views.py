from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, User

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpages_list}
    return render(request,'first_app/index.html', date_dict)


def users(request):
    all_users = User.objects.order_by('first_name')
    return render(request, 'first_app/users.html', context={'all_users':all_users})