from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage
from . import forms

# Create your views here.

def index(request):
    access_list = AccessRecord.objects.order_by('date')
    date_dict = { 'access_records': access_list }
    return render(request, 'first_app/index.html', context=date_dict)

def access_record_view(request):
    form = forms.AccessRecordForm()
    return render(request, 'first_app/access_record_form.html', {'form': form})
