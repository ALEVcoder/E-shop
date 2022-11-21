from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "username", "email", "password1", "password2")

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "email", "username")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=True)

class EmailVerifacationForm(forms.Form):
    code = forms.CharField(max_length=6, required=True)