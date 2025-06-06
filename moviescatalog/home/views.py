import random
from django.shortcuts import render
from movie.models import Movie
from person.models import Person
from genre.models import Genre
from rating.models import Rating
from django.utils.timezone import now
from django.db.models import Avg, Count
from datetime import date
from django.contrib.auth.decorators import login_required

def calcular_estrelas(rating):
  """
  Calcula a exibição de estrelas baseada no rating (0-10).

  Regras:
  - Sem rating (None/0): 5 estrelas vazias
  - Rating 1: meia estrela + 4 vazias
  - Rating 10: 5 estrelas cheias
  - Escala: 0-10 convertida para 0-5 estrelas
  """
  # Se não há rating, mostra 5 estrelas vazias
  if rating is None or rating == 0:
    return {'full': 0, 'half': 0, 'empty': 5}

  # Normaliza de 0-10 para 0-5
  nota_normalizada = rating / 2.0

  # Calcula número de estrelas inteiras
  full = int(nota_normalizada)

  # Calcula se há meia estrela
  restante = nota_normalizada - full
  half = 1 if restante >= 0.5 else 0

  # Ajusta se passou de 5 estrelas
  if full > 5:
    full = 5
    half = 0
  elif full == 5:
    half = 0

  # Calcula estrelas vazias
  empty = 5 - full - half

  return {'full': full, 'half': half, 'empty': empty}

@login_required
def home(request):
  # Filme com maior média de rating (top #1)
  try:
    top_movie = (
      Movie.objects.annotate(
        avg_rating=Avg('ratings__rating'),
        rating_count=Count('ratings__rating')
      )
      .exclude(ratings__rating__isnull=True)
      .order_by('-avg_rating')
      .first()
    )

    if top_movie:
      top_movie.stars = calcular_estrelas(top_movie.avg_rating)
  except Exception as e:
    print(f"Erro ao buscar top movie: {e}")
    top_movie = None

  # Filmes com mais "likes" hoje (excluindo o top #1)
  try:
    today = date.today()
    featured_movies = (
      Movie.objects
      .exclude(id=top_movie.id if top_movie and hasattr(top_movie, 'id') else None)
      .annotate(
        like_count=Count('ratings', filter=Rating.objects.filter(created_at__date=today)),
        avg_rating=Avg('ratings__rating')
      )
      .order_by('-like_count')[:6]
    )

    featured_movies = list(featured_movies)
    while len(featured_movies) % 3 != 0 and len(featured_movies) > 0:
      featured_movies.append(featured_movies[-1])

    for movie in featured_movies:
      movie.stars = calcular_estrelas(movie.avg_rating)

  except Exception as e:
    print(f"Erro ao buscar filmes em destaque: {e}")
    featured_movies = []

  # Buscar atores
  try:
    actors = list(Person.objects.filter(role='Ator').order_by('name'))
    while len(actors) < 10 and actors:
      actors.extend(actors[:10 - len(actors)])
  except Exception as e:
    print(f"Erro ao buscar atores: {e}")
    actors = []

  actors_groups = []
  for i in range(0, len(actors), 10):
    group = actors[i:i + 10]
    while len(group) < 10:
      group.append(group[len(group) % len(group)])
    actors_groups.append(group)

  # Categorias
  try:
    categories = list(Genre.objects.all().order_by('name'))
    if len(categories) < 6 and len(categories) > 0:
      while len(categories) < 6:
        categories.append(categories[len(categories) % len(categories)])
  except Exception as e:
    print(f"Erro ao buscar categorias: {e}")
    categories = []

  for category in categories:
    hue = random.randint(0, 360)
    category.hue = hue

  categories_display_groups = [categories[i:i+6] for i in range(0, len(categories), 6)]

  context = {
    'top_movie': top_movie,
    'featured_movies': featured_movies,
    'featured_movies_groups': [featured_movies[i:i+3] for i in range(0, len(featured_movies), 3)],
    'actors_groups': actors_groups,
    'categories_display_groups': categories_display_groups,
  }

  return render(request, 'home/index.html', context)
