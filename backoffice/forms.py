from django import forms
from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AuthorForm(forms.ModelForm):
    model = Author
    fields = ['author', 'year_born']

class LoginForm(forms.Form):
    username = forms.CharField(min_length=1)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']