from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class ManagerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ManagerLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"
        self.fields['password'].label = "Пароль"