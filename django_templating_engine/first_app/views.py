from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'message': 'Hello I am from first_app.views.index'}
    return render(request, 'first_app/index.html', context=my_dict)
