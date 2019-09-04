from django.contrib import admin
from django.urls import path, include
from school import views

app_name = 'school_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('schools', views.school_list, name='school-list'),
    path('<str:test>', views.url_test, name='url-test'),
]