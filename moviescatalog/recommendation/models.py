from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommended_to')
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendação para {self.user.username}: {self.movie.title}"
