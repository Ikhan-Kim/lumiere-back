from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie, MovieRankComment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'vote_average', 'poster_path', 'genres')

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieRankCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRankComment
        fields = ('rank', 'content', 'user', 'movie')
        