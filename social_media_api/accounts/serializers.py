from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import  User
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = "__all__"



"serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"