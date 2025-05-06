from django.db import models
from genre.models import Genre
from person.models import Person

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    synopsis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    people = models.ManyToManyField(Person, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
