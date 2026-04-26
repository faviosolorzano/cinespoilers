from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, ReviewViewSet # CAMBIO

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)  # NUEVO
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls