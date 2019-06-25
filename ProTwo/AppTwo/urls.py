from django.urls import path
from .views import home, _help

urlpatterns = [
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('help/', _help, name='help')
]
