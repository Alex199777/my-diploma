from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserLogin(AuthenticationForm):
    class Meta:
        model = User


class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']
    username = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class UserProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']

    username = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()



