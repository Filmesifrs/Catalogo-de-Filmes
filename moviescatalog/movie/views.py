from django.shortcuts import render, get_object_or_404
from movie.models import Movie
from django.db.models import Avg

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    # Separar diretores e atores
    people = movie.people.all()
    directors = [p.name for p in people if p.role == 'Diretor']
    actors = [p.name for p in people if p.role == 'Ator']

    # Gêneros
    genres = list(movie.genres.values_list('name', flat=True))

    print(genres)
    # Avaliações
    ratings = movie.ratings.all()
    total_ratings = ratings.count()
    avg_rating_10 = ratings.aggregate(avg=Avg('rating'))['avg'] or 0
    avg_rating = round(avg_rating_10 / 2, 1)

    context = {
        'title': movie.title,
        'genres': genres,
        'release_year': movie.release_year,
        'synopsis': movie.synopsis,
        'directors': directors,
        'actors': actors,
        'avg_rating': avg_rating,
        'total_ratings': total_ratings,
        'poster_url': movie.poster.url if movie.poster else None,
    }

    return render(request, 'movie/details.html', context)