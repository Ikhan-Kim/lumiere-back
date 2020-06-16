from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie, MovieRankComment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average', 'poster_path', 'genres', 'backdrop_path')

class MovieRankCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = MovieRankComment
        # fields = '__all__'
        exclude = ['movie']
        
class MovieDetailSerializer(serializers.ModelSerializer):
    comments = MovieRankCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'