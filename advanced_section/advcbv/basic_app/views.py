from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.
# def home(request):
#     return render(request, 'basic_app/index.html')


class HomePage(TemplateView):
    template_name = 'basic_app/index.html'
    def get(self, request):
        return render(request, self.template_name)