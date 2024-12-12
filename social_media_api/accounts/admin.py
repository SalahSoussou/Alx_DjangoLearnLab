from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
  # form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('username', 'bio', )}),
  )

  list_display = ['username']
  search_fields = ('username',)
  ordering = ('username',)
admin.site.register(User, UserAdmin)