from django.db.models import Avg
from rest_framework import serializers
from .models import Movie, Genre, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["created_at"]
        
class MovieSerializer(serializers.ModelSerializer):

    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
    
