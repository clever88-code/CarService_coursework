# from botTG import token, chat_id
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from requests import request
from core.models import Cars
from record.forms import CarForm, RecordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
import telebot




class RecordView(TemplateView):
    template_name = 'record.html'


    def get(self, request, *args, **kwargs):
        car_form = CarForm
        record_form = RecordForm(user_id=request.user.id)
        context = self.get_context_data(**kwargs)
        # record_form.car.queryset = Cars.objects.filter(auth_user_id=request.user.id)
        context['car_form'] = car_form
        context['record_form'] = record_form
        return self.render_to_response(context)


class CarFormView(FormView):
    template_name = 'record.html'
    form_class = CarForm
    success_url = '/record'


    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = self.request.user.id


        return super().form_valid(form)


class RecordFormView(FormView):
    template_name = 'record.html'
    form_class = RecordForm
    success_url = reverse_lazy('record:record')



def add_record_view(request):
    if request.POST:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            form.save()
    return redirect('/record/')


def add_car_view(request):
    if request.POST:
        form = CarForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()
    return redirect('/record/')
