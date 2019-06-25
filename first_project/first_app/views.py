from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "Hello IM FROM FirstApp"}
    return render(request, 'firstapp/index.html', context=my_dict)