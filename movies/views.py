from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, MovieRankComment
from .serializers import MovieListSerializer, MovieDetailSerializer, MovieRankCommentSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)