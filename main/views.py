#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse ("<h4>проверка работа</h4>")

def login(request):
    return HttpResponse ("<h4>тип логин</h4>")

def admin(request):
    return HttpResponse ("<h4>тип админка</h4>")