import telebot
from django.shortcuts import render, redirect
from django.views.generic import FormView
import asyncio

from aiogram import Bot, types
from orders.forms import OrderForm





# Create your views here.
class OrderFormView(FormView):
    template_name = 'orders.html'
    form_class = OrderForm
    success_url = '/orders'


def add_orders(request):
    if request.POST:
        form = OrderForm(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()


    return redirect('/orders/')


