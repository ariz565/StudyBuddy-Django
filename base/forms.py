from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


# Custom form for user registration
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]


# Custom form for room creation
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]


# Form for user profile
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]
