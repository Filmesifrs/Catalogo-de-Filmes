from django.db import models

class Person(models.Model):
    ROLE_CHOICES = (
        ('Ator', 'Ator'),
        ('Diretor', 'Diretor'),
    )
    name = models.CharField(max_length=255)  
    bio = models.TextField()
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='people_photos/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"
