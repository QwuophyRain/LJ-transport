from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from . models import UserProfile
from django.forms import ModelForm, TextInput, Textarea, EmailInput, FileInput



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'User name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last name'}),
            'password': TextInput(attrs={'class': 'input', 'placeholder': 'New Password'}),

        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'iD_Type', 'cardNumber', 'address', 'city', 'country', 'image']
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'iD_Type': TextInput(attrs={'class': 'input', 'placeholder': 'ID type'}),
            'cardNumber': TextInput(attrs={'class': 'input', 'placeholder': 'Card Number'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'City'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'Country'}),
        }






