from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView ,FormView
from core.models import CarMarks, Cars, Firms
from record.forms import CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms





class CarFormView(FormView):
    template_name = 'record.html'
    form_class = CarForm
    success_url = '/record'

    def form_valid(self, form):
        

        Cars.objects.create(**form.cleaned_data)
        return super().form_valid(form)