
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from . import views
# from .views import User_viwe
urlpatterns = [
  path('',views.User_viwe.as_view(),name='user' ),
]

"login/", "register/"