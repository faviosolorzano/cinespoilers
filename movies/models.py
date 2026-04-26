from django.db import models

class Genre(models.Model):  # NUEVO
    name = models.CharField(max_length=100, unique=True)  # NUEVO

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    genres = models.ManyToManyField(Genre, related_name='movies')  # NUEVO

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.rating}"