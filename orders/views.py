import telebot
from django.shortcuts import render, redirect
from django.views.generic import FormView

from orders.forms import OrderForm

token = "5948617624:AAHk3AaEtMwANEwWLBdACn9kgV09Vk9iOSs"

chat_id = '1015269507'


# Create your views here.
class OrderFormView(FormView):
    template_name = 'orders.html'
    form_class = OrderForm
    success_url = '/orders'
    bot = telebot.TeleBot(token)


def add_orders(request):
    if request.POST:
        form = OrderForm(data=request.POST)
        bot = telebot.TeleBot(token)
        bot.send_message(chat_id=chat_id, text='Выполнена работа для заказа!🔥🔥🔥')
        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()
    return redirect('/orders/')
