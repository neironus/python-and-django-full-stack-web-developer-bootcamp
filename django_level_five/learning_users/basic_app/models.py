from django.db import models
from django.shortcuts import reverse
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# from .views import profile_user
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics', blank=True)
    # slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        '''  
        Если использовать namespace тогда нужно использвать basic_app:profile-user вместо profile-user
        return reverse('basic_app:profile-user', kwargs={"user_name": self.user})
        reverse('имя урла из urls.py', kwargs={"переменная user_name из profile/<str:user_name>": self.user})
        или так
        return reverse('basic_app.views.profile_user', kwargs={"user_name": self.user.username})
        '''
        # return reverse('basic_app:profile-user', kwargs={"user_name": self.user.username})
        return reverse('basic_app.views.profile_user', kwargs={"user_name": self.user.username})

    def __str__(self):
        return self.user.username
