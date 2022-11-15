from django.shortcuts import render
from . import views


def record_home(request):
    return render(request, 'record/record_home.html')