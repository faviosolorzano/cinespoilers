from rest_framework.viewsets import ModelViewSet
from .models import Movie, Genre  # CAMBIO
from .serializers import MovieSerializer, GenreSerializer  # CAMBIO

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(ModelViewSet):  # NUEVO
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer