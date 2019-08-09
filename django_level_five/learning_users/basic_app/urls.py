from django.urls import path
from .views import home, login_user, sign_up

app_name = 'basic_app'
urlpatterns = [
    path('', home, name='home'),
    path('login', login_user, name='login-user'),
    path('sign-up', sign_up, name='sign-up')
]
