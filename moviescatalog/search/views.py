from django.shortcuts import render
from django.db.models import Q
from movie.models import Movie
from .forms import MovieSearchForm
import re

def search_movies(request):
  form = MovieSearchForm(request.GET)
  movies = Movie.objects.all()

  genre = request.GET.get('genre')
  actor = request.GET.get('actor')

  if genre:
    movies = movies.filter(genres__name__iexact=genre).distinct()

  elif actor:
    movies = movies.filter(people__name__iexact=actor, people__role='Ator').distinct()

  elif form.is_valid():
    q = form.cleaned_data.get('query')
    if q:
      q_cleaned = re.sub(r'[^\w\s]', '', q).strip()

      filters = Q(title__icontains=q) | \
                Q(title__icontains=q_cleaned) | \
                Q(synopsis__icontains=q) | \
                Q(genres__name__icontains=q) | \
                Q(people__name__icontains=q)

      # Se for número, adiciona filtro por ano
      if q_cleaned.isdigit():
        filters |= Q(release_year__icontains=q_cleaned)

      movies = movies.filter(filters).distinct()

  return render(request, 'search/results.html', {'form': form, 'movies': movies})