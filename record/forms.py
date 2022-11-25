from django import forms
from django.core.exceptions import ValidationError
from requests import request

from core.models import AuthUser, Cars, Records


class CarForm(forms.ModelForm):
    # if request.method == 'POST':
    #   form = BillSelectForm(request.POST)
    #   if form.is_valid():
    #        bill = Bill.objects.get(form.cleaned_data['pk'])
    # else:
    #    form = BillSelectForm()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car_number'].widget.attrs.update({'placeholder': 'Введите гос.номер'})
        self.fields['firms'].widget.attrs.update({'placeholder': 'Введите название фирмы'})
        self.fields['mark'].widget.attrs.update({'placeholder': 'Введите марку автомибиля'})

    class Meta:
        model = Cars
        fields = ['car_number', 'firms', 'mark']


class RecordForm(forms.ModelForm):
    # if request.method == 'POST':
    #   form = BillSelectForm(request.POST)
    #   if form.is_valid():
    #        bill = Bill.objects.get(form.cleaned_data['pk'])
    # else:
    #    form = BillSelectForm()
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Введите описание проблемы', 'rows': '2'})
        self.fields['car'].queryset = Cars.objects.filter(auth_user_id=user_id)

    class Meta:
        model = Records
        fields = ['car', 'date', 'description']
