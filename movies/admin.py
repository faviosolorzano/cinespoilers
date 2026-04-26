from django.contrib import admin
from .models import Movie, Genre  # CAMBIO

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'release_date', 'created_at')
    search_fields = ('title',)
    list_filter = ('release_date',)
    filter_horizontal = ('genres',)  # NUEVO

@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)