from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class MyRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'block w-full p-4 text-lg rounded-lg bg-black'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'block w-full p-4 text-lg rounded-lg bg-black'}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username','class': 'block w-full p-4 text-lg rounded-lg bg-black'}),max_length=100)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password','class': 'block w-full p-4 text-lg rounded-lg bg-black'}),max_length=100)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm password', 'class': 'block w-full p-4 text-lg rounded-lg bg-black'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'block w-full p-4 text-lg rounded-lg bg-black'}),required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username','class': 'block w-full p-4 text-lg rounded-lg bg-black'}),max_length=100)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password','class': 'block w-full p-4 text-lg rounded-lg bg-black'}),max_length=100)
    class Meta:
        model = User
        fields = ('username', 'password')
        

