from django.shortcuts import render
from .forms import UserForm, UserProfileForm

# Create your views here.
def home(request):
    print('*' * 5)
    print(request.META.get('HTTP_X_REAL_IP') or request.META.get('REMOTE_ADDR'))
    print('*' * 5)
    return render(request, 'basic_app/index.html',
            {
                'user_form': UserForm,
                'user_profile': UserProfileForm
            }
        )