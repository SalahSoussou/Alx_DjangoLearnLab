

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


"comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"
"tags/<slug:tag_slug>/", "PostByTagListView.as_view()"