from django.shortcuts import render
from .models import *

# Create your views here.


class User_viwe():
    users = User.objects.all()
    return render(request , )