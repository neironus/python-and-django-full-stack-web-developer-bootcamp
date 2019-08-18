from django.urls import path
# from django.contrib.auth import 
from .views import home, login_user, sign_up, logout_user, profile_user

app_name = 'basic_app'
urlpatterns = [
    path('', home, name='home'),
    path('login', login_user, name='login-user'),
    path('sign-up', sign_up, name='sign-up'),
    path('logout', logout_user, name='logout-user'),
    path('profile/<str:user_name>', profile_user, name='profile-user')
]
