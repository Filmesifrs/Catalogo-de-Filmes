from django.shortcuts import render
from django.db.models import Q
from movie.models import Movie
from .forms import MovieSearchForm

def search_movies(request):
  form = MovieSearchForm(request.GET)
  movies = Movie.objects.all()

  if form.is_valid():
    q = form.cleaned_data.get('query')
    if q:
      movies = movies.filter(
        Q(title__icontains=q) |
        Q(title__iregex=rf'\b{q}\b') |
        Q(synopsis__icontains=q) |
        Q(genres__name__icontains=q) |
        Q(people__name__icontains=q)
      ).distinct()

  return render(request, 'search/results.html', {'form': form, 'movies': movies})
