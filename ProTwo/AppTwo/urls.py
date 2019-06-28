from django.urls import path
from .views import home, _help, users

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('users/', users, name='users'),
    path('help/', _help, name='help')
]
