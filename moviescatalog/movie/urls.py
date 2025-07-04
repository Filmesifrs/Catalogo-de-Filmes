from django.urls import path
from .views import movie_detail
from rating.views import submit_rating

urlpatterns = [
  path('<int:movie_id>', movie_detail, name='movie_detail'),
  path('<int:movie_id>/rate/', submit_rating, name='submit_rating'),
]
