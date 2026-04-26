from rest_framework.viewsets import ModelViewSet
from .models import Movie, Genre, Review  # CAMBIO
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer  # CAMBIO
from rest_framework import viewsets
from django.db.models import Avg

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().prefetch_related('reviews')
    serializer_class = MovieSerializer
    
class GenreViewSet(ModelViewSet):  # NUEVO
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer