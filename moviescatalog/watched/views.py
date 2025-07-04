from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.views.decorators.http import require_POST

from movie.models import Movie
from watched.models import Watched

@login_required
@require_POST
def toggle_watched(request):
    movie_id = request.POST.get('movie_id')

    if not movie_id:
        messages.error(request, "ID do filme não informado.")
        return JsonResponse({"status": "error", "message": "ID do filme é obrigatório."}, status=400)

    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        messages.error(request, "Filme não encontrado.")
        return JsonResponse({"status": "error", "message": "Filme não encontrado."}, status=404)

    watched_entry = Watched.objects.filter(user=request.user, movie=movie).first()

    if watched_entry:
        watched_entry.delete()
        messages.success(request, f'"{movie.title}" desmarcado como assistido.')
        return JsonResponse({"status": "success", "watched": False, "message": f'"{movie.title}" desmarcado.'})
    else:
        Watched.objects.create(
            user=request.user,
            movie=movie,
            times_watched=1,
            watched_date=now().date()
        )
        messages.success(request, f'"{movie.title}" marcado como assistido com sucesso!')
        return JsonResponse({"status": "success", "watched": True, "message": f'"{movie.title}" marcado como assistido.'})