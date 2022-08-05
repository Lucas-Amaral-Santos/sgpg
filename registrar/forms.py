from django.contrib.auth.models import User
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label = 'Nome do usuário')
    password = forms.CharField(label = 'Senha', widget = forms.PasswordInput)
