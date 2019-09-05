from django.contrib import admin
from django.urls import path, include
from school import views

app_name = 'school_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('schools', views.school_list, name='school-list'),
    path('<int:pk>', views.school_description, name='school-description'),
    path('<int:pk>/update', views.school_edit, name='school-edit'),
]