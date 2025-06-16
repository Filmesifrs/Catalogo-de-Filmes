from django.shortcuts import render, get_object_or_404
from .models import Movie  


from django.db.models import Avg

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Movie, id=filme_id)

    diretor = filme.people.filter(role='director').first()
    elenco = filme.people.filter(role='actor')

    # Calcula a média da nota (rating)
    nota_media = filme.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']

    context = {
        'filme': filme,
        'diretor': diretor,
        'elenco': elenco,
        'nota_media': nota_media,
    }
    return render(request, 'movie/detalhe_filme.html', context)