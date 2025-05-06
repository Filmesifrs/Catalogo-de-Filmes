from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

class Watched(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watched_movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watched_by')
    times_watched = models.IntegerField(default=1)
    watched_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} assistiu {self.movie.title} ({self.times_watched}x)"
