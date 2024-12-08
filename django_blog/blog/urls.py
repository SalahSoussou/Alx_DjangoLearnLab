from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("register/", views.register_view, name='register'),
    # path("login/", views.login_view, name='login'),
    # path("profile/", views.profile_view, name='profile'),
    # path("logout/", views.logout_view, name='logout'),
]


"post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"