from django import forms
from django.core.exceptions import ValidationError

from core.models import Firms,CarMarks,Cars

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars 
        fields = ['car_number']


