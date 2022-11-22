from django import forms
from django.core.exceptions import ValidationError
from requests import request

from core.models import AuthUser, Cars

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars 
        fields = ['car_number','firms', 'mark']



