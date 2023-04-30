from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'first_name', 'last_name', 'birthday', 'password1', 'password2']
        help_texts = {'username': None, 'password1': None, 'password2': None}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
