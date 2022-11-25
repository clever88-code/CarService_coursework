#from botTG import token, chat_id
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from requests import request
from core.models import Cars
from record.forms import CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
import telebot


token = "5948617624:AAHk3AaEtMwANEwWLBdACn9kgV09Vk9iOSs"

chat_id = '1015269507'


class CarFormView(FormView):
    template_name = 'record.html'
    form_class = CarForm
    success_url = '/record'
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id=chat_id, text = 'Сайт включен/перезапушен!🔥🔥🔥')
    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = self.request.user.id
            obj.save()
            bot = telebot.TeleBot(token)
            bot.send_message(chat_id=chat_id, text = 'Посмотри админ панель новая заявка!🔥🔥🔥')

           
        return super().form_valid(form)
