from django.shortcuts import render, get_object_or_404
from movie.models import Movie
from watched.models import Watched
from rating.models import Rating
from django.db.models import Avg
from home.views import calcular_estrelas
from django.contrib.auth.decorators import login_required

@login_required
def movie_detail(request, movie_id):
  movie = get_object_or_404(Movie, id=movie_id)

  # Separar diretores e atores
  people = movie.people.all()
  directors = [p.name for p in people if p.role == 'Diretor']
  actors = [p.name for p in people if p.role == 'Ator']

  # Gêneros
  genres = list(movie.genres.values_list('name', flat=True))
  edit_mode = request.GET.get("edit") == "true"

  # Avaliações
  ratings = Rating.objects.filter(movie=movie).order_by('-created_at')
  total_ratings = ratings.count()
  avg_rating = ratings.aggregate(avg=Avg('rating'))['avg'] or 0
  avg_rating = round(avg_rating, 1)

  # Prepara avaliações com estrelas
  ratings_data = []
  for rating in ratings:
    ratings_data.append({
      'user': rating.user,
      'rating': rating.rating,
      'review': rating.review,
      'created_at': rating.created_at,
      'stars': calcular_estrelas(rating.rating)
    })

  watched = Watched.objects.filter(user=request.user, movie=movie).exists()
  user_rating = Rating.objects.filter(movie=movie, user=request.user).first()

  context = {
    'movie_id': movie.id,
    'title': movie.title,
    'genres': genres,
    'release_year': movie.release_year,
    'synopsis': movie.synopsis,
    'directors': directors,
    'actors': actors,
    'avg_rating': avg_rating,
    'total_ratings': total_ratings,
    'ratings': ratings_data,
    'poster_url': movie.poster.url if movie.poster else None,
    'watched': watched,
    'edit': edit_mode,
    'user_rating': user_rating,
  }

  return render(request, 'movie/details.html', context)