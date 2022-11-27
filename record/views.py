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

token = "5948617624:AAHk3AaEtMwANEwWLBdACn9kgV09Vk9iOSs"

chat_id = '1015269507'


class RecordView(TemplateView):
    template_name = 'record.html'
    bot = telebot.TeleBot(token)

    def get(self, request, *args, **kwargs):
        car_form = CarForm
        record_form = RecordForm(user_id=request.user.id)
        context = self.get_context_data(**kwargs)
        # record_form.car.queryset = Cars.objects.filter(auth_user_id=request.user.id)
        context['car_form'] = car_form
        context['record_form'] = record_form
        return self.render_to_response(context)

    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            car = Cars(car_number=form.cleaned_data['car_number'],
                       auth_user=request.user,
                       firms=form.cleaned_data['firms'],
                       mark=form.cleaned_data['mark'],
                       commit=False)
            car.save()
            return HttpResponse("Car added")  # По хорошему тут что то заюзать по типу flash во flask
        return HttpResponse("Super string")  # Кидай на это же класс но метод GET
        # Code here


class CarFormView(FormView):
    template_name = 'record.html'
    form_class = CarForm
    success_url = '/record'
    bot = telebot.TeleBot(token)

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = self.request.user.id
            obj.save()
            bot = telebot.TeleBot(token)
            bot.send_message(chat_id=chat_id, text='Добавлен автомобиль!🔥🔥🔥')
        return super().form_valid(form)


class RecordFormView(FormView):
    template_name = 'record.html'
    form_class = RecordForm
    success_url = reverse_lazy('record:record')
    bot = telebot.TeleBot(token)

    # def form_valid(self, form):
    #     print('asdasd')
    #     if form.is_valid():
    #         bot = telebot.TeleBot(token)
    #         bot.send_message(chat_id=chat_id, text='Есть заполненная запись!🔥🔥🔥')
    #
    #     return super().form_valid(form)


def add_record_view(request):
    if request.POST:
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/record/')
