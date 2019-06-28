from django import forms
from .models import User

class  Users(forms.Form):
    first_name = forms.CharField(label="First name", max_length=56)
    last_name = forms.CharField(label="Last name", max_length=56)
    email = forms.EmailField(label="Your email")

    