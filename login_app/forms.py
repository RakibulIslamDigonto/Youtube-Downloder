from django import forms
from .models import CreateUser


class CreateFrom(forms.Form):
    full_name = forms.CharField(label='Full Name', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))

    user_name = forms.CharField(label='User Name', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Enter your User name'}))
    
    email = forms.EmailField(label='Email', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))
    
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))
    
    image = forms.ImageField(label='Image', required=False)
    

