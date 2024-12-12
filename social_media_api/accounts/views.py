from django.shortcuts import render
from .models import *
from django.contrib.auth.views import LoginView

# Create your views here.


class User_viwe(LoginView):
    users = User.objects.all()