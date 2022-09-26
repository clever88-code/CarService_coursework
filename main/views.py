from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return render(request, 'main/index.html' )

def login(request):
    return render(request, 'main/about.html' )

def admin(request):
    return HttpResponse ("<h4>тип админка</h4>")