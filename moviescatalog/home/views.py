from django.shortcuts import render
from movie.models import Movie

def home(request):
  """
  View para renderizar a tela inicial com o filme principal (Top #1) e filmes em destaque
  """
  try:
    top_movie = Movie.objects.first()
  except Exception as e:
    print(f"Erro ao buscar filme principal: {e}")
    top_movie = None

  try:
    featured_movies = list(Movie.objects.all())
    while len(featured_movies) % 3 != 0 and len(featured_movies) > 0:
      featured_movies.append(featured_movies[-1])

  except Exception as e:
    print(f"Erro ao buscar filmes em destaque: {e}")
    featured_movies = []

  context = {
    'top_movie': top_movie,
    'featured_movies': featured_movies,
    'featured_movies_groups': [featured_movies[i:i+3] for i in range(0, len(featured_movies), 3)]
  }

  return render(request, 'home/index.html', context)
