from first_app.models import Webpage
from django import forms

class AccessRecordForm(forms.Form):
    webpage = forms.ModelChoiceField(Webpage.objects.order_by('-name'))
    date = forms.DateField()