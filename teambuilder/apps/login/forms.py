from django.contrib.auth.forms import AuthenticationForm
from django import forms

class loginForm(AuthenticationForm):
    username = forms.EmailField(error_messages={'required':'An email is required.', 'invalid':'That\'s not a valid email.'},
        widget=forms.TextInput(attrs={'autocomplete':'off', 'placeholder':'Email', 'style':'', 'class':'form-control '}),
    )
    password = forms.CharField(error_messages={'required':'A password is required.'},
        widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style':'', 'class':'form-control'}),
    )
    error_messages = {'invalid_login':'The provided information isn\'t valid.', 'inactive':'The account isn\'t active.'}