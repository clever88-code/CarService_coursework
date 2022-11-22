from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('accounts/login/', auth.views.LoginView.as_view(), name="login"),
    path('accounts/logout/', auth.views.LogoutView.as_view(), name="logout"),
    path("accounts/registration/", CreateView.as_view(form_class=UserCreationForm,
                                                      success_url=reverse_lazy("login"),
                                                      template_name="registration/registration.html"),
         name="registration"),
]
