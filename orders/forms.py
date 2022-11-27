from django import forms
from django.core.exceptions import ValidationError
from requests import request

from core.models import AuthUser, Records, Orders


class OrderForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['completed_work'].widget.attrs.update({'placeholder': 'Укажите выполненную работу'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Введите сколько стоит работа','min':0})

    class Meta:
        model = Orders
        fields = ['record', 'completed_work', 'price']
