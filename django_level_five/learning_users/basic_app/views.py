from django.shortcuts import render
from .forms import UserForm, UserProfileForm

# Create your views here.
def home(request):
    return render(request, 'basic_app/index.html',
            {
                'user_form': UserForm,
                'user_profile': UserProfileForm
            }
        )