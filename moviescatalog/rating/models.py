from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} avaliou {self.movie.title} ({self.rating}/10)"
