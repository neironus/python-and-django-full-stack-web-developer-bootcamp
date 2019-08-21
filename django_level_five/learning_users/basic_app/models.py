from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics', blank=True)
    # slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.user})
    


    def __str__(self):
        return self.user.username
