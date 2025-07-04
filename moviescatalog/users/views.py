from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Avg

from watched.models import Watched
from rating.models import Rating

from collections import Counter
from home.views import calcular_estrelas

from .forms import CustomLoginForm, CustomRegisterForm, CustomPasswordChangeForm

def home(request):
  return render(request, 'base.html')

from django.db.models import Avg, Max
from rating.models import Rating

@login_required
def perfil(request):
  usuario = request.user

  if request.method == 'POST':
    usuario.email = request.POST.get('email')
    nome_completo = request.POST.get('nome')
    if nome_completo:
      partes = nome_completo.strip().split(' ', 1)
      usuario.first_name = partes[0]
      usuario.last_name = partes[1] if len(partes) > 1 else ''

    usuario.save()
    messages.success(request, 'Perfil atualizado com sucesso!')
    return redirect('users:perfil')

  total_ratings = Rating.objects.filter(user=usuario).count()
  average_rating = Rating.objects.filter(user=usuario).aggregate(avg=Avg('rating'))['avg'] or 0

  melhor_avaliacao = (
    Rating.objects.filter(user=usuario)
    .order_by('-rating', '-created_at')
    .select_related('movie')
    .first()
  )
  melhor_filme = melhor_avaliacao.movie.title if melhor_avaliacao else 'Nenhum'

  # Filmes assistidos pelo usuário
  assistidos = Watched.objects.filter(user=usuario).select_related('movie').prefetch_related('movie__genres', 'movie__people')

  # Gênero mais assistido
  genero_counter = Counter()
  ator_counter = Counter()

  for entrada in assistidos:
    movie = entrada.movie
    for genero in movie.genres.all():
      genero_counter[genero.name] += 1
    for pessoa in movie.people.all():
      if pessoa.role == 'Ator':
        ator_counter[pessoa.name] += 1

  genero_mais_assistido = genero_counter.most_common(1)[0][0] if genero_counter else 'Nenhum'
  ator_mais_assistido = ator_counter.most_common(1)[0][0] if ator_counter else 'Nenhum'

  context = {
    'usuario': usuario,
    'total_ratings': total_ratings,
    'average_rating': round(average_rating, 1),
    'melhor_filme': melhor_filme,
    'genero_mais_assistido': genero_mais_assistido,
    'ator_mais_assistido': ator_mais_assistido,
  }
  return render(request, 'users/perfil.html', context)

@login_required
def minhas_avaliacoes(request):
  avaliacoes = Rating.objects.filter(user=request.user).select_related("movie").order_by("-created_at")

  for avaliacao in avaliacoes:
    estrelas = calcular_estrelas(avaliacao.rating)
    avaliacao.full_stars = estrelas['full']
    avaliacao.half_star = estrelas['half']
    avaliacao.empty_stars = estrelas['empty']

  return render(request, "users/reviews.html", {"avaliacoes": avaliacoes})

def logout_view(request):
  logout(request)
  list(get_messages(request))
  return redirect('users:login')

def login_view(request):
  list(get_messages(request))
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
      full_name = form.cleaned_data.get('full_name')
      if full_name:
        partes = full_name.strip().split(' ', 1)
        user.first_name = partes[0]
        user.last_name = partes[1] if len(partes) > 1 else ''
        user.save()
      login(request, user)
      return redirect('/')
    else:
      print(form.errors)
      list(get_messages(request))
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
