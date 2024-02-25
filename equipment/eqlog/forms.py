from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from eqlog.models import Person, Equipment


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class FilterPersonForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=50, required=False)
    first_name = forms.CharField(label='Имя', max_length=50, required=False)