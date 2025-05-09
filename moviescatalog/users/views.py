from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import CustomLoginForm, CustomRegisterForm, CustomPasswordChangeForm

def login_view(request):
  if request.method == 'POST':
    form = CustomLoginForm(request, data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
      return redirect('/')
    else:
      messages.error(request, "Nome de usuário ou senha inválidos.")
  else:
      form = CustomLoginForm(request)
  return render(request, 'users/login.html', {'form': form})

def register_view(request):
  if request.method == 'POST':
    form = CustomRegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      print(form.errors)
      messages.error(request, "Erro no cadastro. Verifique os dados.")
  else:
    form = CustomRegisterForm()
  return render(request, 'users/register.html', {'form': form})

def change_password(request):
  form = CustomPasswordChangeForm(user=request.user, data=request.POST or None)
  if request.method == 'POST':
      if form.is_valid():
          user = form.save()
          update_session_auth_hash(request, user)
          messages.success(request, 'Senha atualizada com sucesso!')
          return redirect('login')
      else:
          messages.error(request, 'Corrija os erros abaixo.')
  return render(request, 'users/change_password.html', {'form': form})
