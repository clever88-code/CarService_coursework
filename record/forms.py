from django import forms
from django.core.exceptions import ValidationError
from requests import request

from core.models import AuthUser, Cars

class CarForm(forms.ModelForm):


    #if request.method == 'POST':
    #   form = BillSelectForm(request.POST)
    #   if form.is_valid():
    #        bill = Bill.objects.get(form.cleaned_data['pk'])
    #else:
    #    form = BillSelectForm()

    class Meta:
        model = Cars 
        fields = ['car_number','firms', 'mark','auth_user']

        


