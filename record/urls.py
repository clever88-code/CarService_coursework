from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import RecordView, RecordFormView, add_record_view, add_car_view

app_name = "record"

urlpatterns = [
    path('', RecordView.as_view(), name="record"),
    path('add-record', add_record_view, name='add_record'),
    path('add-car', add_car_view, name='add_car'),
]
