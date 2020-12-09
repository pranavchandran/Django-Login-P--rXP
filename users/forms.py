from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = "User Name")
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label = "Email")