from django.shortcuts import render
from movie.models import Movie
from rating.models import Rating
from django.utils.timezone import now
from django.db.models import Avg, Count
from datetime import date

def home(request):
    # Filme com maior média de rating (top #1)
    try:
        top_movie = (
            Movie.objects.annotate(avg_rating=Avg('ratings__rating'))
            .exclude(ratings__rating__isnull=True)
            .order_by('-avg_rating')
            .first()
        )
    except Exception as e:
        print(f"Erro ao buscar top movie: {e}")
        top_movie = None

    # Filmes com mais "likes" hoje (excluindo o top #1)
    try:
        today = date.today()
        featured_movies = (
            Movie.objects
            .exclude(id=top_movie.id if top_movie else None)
            .annotate(like_count=Count('ratings', filter=(
                Rating.objects.filter(created_at__date=today)
            )))
            .order_by('-like_count')[:6]
        )

        # Preencher grupo de 3
        featured_movies = list(featured_movies)
        while len(featured_movies) % 3 != 0 and len(featured_movies) > 0:
            featured_movies.append(featured_movies[-1])

    except Exception as e:
        print(f"Erro ao buscar filmes em destaque: {e}")
        featured_movies = []

    context = {
        'top_movie': top_movie,
        'featured_movies': featured_movies,
        'featured_movies_groups': [featured_movies[i:i + 3] for i in range(0, len(featured_movies), 3)],
    }

    return render(request, 'home/index.html', context)
