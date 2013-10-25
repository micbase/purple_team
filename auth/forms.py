
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Password'
        }))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email Address'
        }))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your First Name'
        }))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Last Name'
        }))

    def clean_username(self):
        count = User.objects.filter(
            username__exact=self.cleaned_data['username']).count()
        if count >= 1:
            raise forms.ValidationError("This username has been taken")
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        count = User.objects.filter(
            email__exact=self.cleaned_data['email']).count()
        if count >= 1:
            raise forms.ValidationError("This email has been used")
        else:
            return self.cleaned_data['email']

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            )
        user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Password'
        }))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data.get('username', None),
            password=self.cleaned_data.get('password', None),
        )
        if self.user and self.user.is_active:
            return self.user
        else:
            self._errors['login'] = "Login fails, username and password do not match"
            forms.ValidationError("Login Error")

    def save(self):
        return self.user
