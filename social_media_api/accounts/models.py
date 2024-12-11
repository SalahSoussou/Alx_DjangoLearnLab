from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date



  # username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  # email = models.EmailField(_('email address'), unique = True)
  # native_name = models.CharField(max_length = 5)
  # phone_no = models.CharField(max_length = 10)
  # USERNAME_FIELD = 'email'
  # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  bio= models.TextField()
  profile_picture = models.ImageField()
  followers = models.ManyToManyField(symmetrical=False,to='User')
  def __str__(self):
      return "{}".format(self.username)