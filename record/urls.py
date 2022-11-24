from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import CarFormView

app_name = "record"

urlpatterns = [
    path('', CarFormView.as_view(), name="record")
]
