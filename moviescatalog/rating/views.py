from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import Avg
from django.contrib.auth.models import User
from movie.models import Movie
from rating.models import Rating
import json

@login_required
@require_http_methods(["POST"])
def submit_rating(request, movie_id):
  try:
    movie = get_object_or_404(Movie, id=movie_id)
    data = json.loads(request.body)

    rating_value = int(data.get("rating", 0))
    review_text = data.get("review", "").strip()

    # Validar nota (1-10)
    if rating_value < 1 or rating_value > 10:
      return JsonResponse({"success": False, "error": "Nota deve ser entre 1 e 10"})

    # Verificar se o usuário já avaliou este filme
    existing_rating = Rating.objects.filter(user=request.user, movie=movie).first()

    if existing_rating:
      # Atualizar avaliação existente
      existing_rating.rating = rating_value
      existing_rating.review = review_text if review_text else None
      existing_rating.save()
    else:
      # Criar nova avaliação
      Rating.objects.create(
        user=request.user,
        movie=movie,
        rating=rating_value,
        review=review_text if review_text else None
      )

    # Buscar todas as avaliações atualizadas
    ratings = Rating.objects.filter(movie=movie).order_by("-created_at")

    # Calcular nova média
    avg_rating = ratings.aggregate(avg=Avg("rating"))["avg"] or 0
    avg_rating = round(avg_rating, 1)

    # Preparar dados das avaliações para retorno
    ratings_data = []
    for rating in ratings:
      ratings_data.append({
        "username": rating.user.username,
        "rating": rating.rating,
        "review": rating.review,
        "created_at": rating.created_at.strftime("%d/%m/%Y")
      })

    return JsonResponse({
      "success": True,
      "avg_rating": avg_rating,
      "ratings": ratings_data
    })

  except Exception as e:
    return JsonResponse({"success": False, "error": str(e)})
