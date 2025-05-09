from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'})
    )

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomPasswordChangeForm(PasswordChangeForm):
  new_password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder': 'Nova senha', 'class': 'form-control'})
  )
  new_password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirme Senha', 'class': 'form-control'})
  )
