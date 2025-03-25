# In myapp/forms.py
from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
