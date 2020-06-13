from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Article, ArticleComment
from .serializers import ArticleCommentSerializer, ArticleSerializer, ArticleDetailSerializer, ArticleListSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_id):
    article_data = get_object_or_404(Article, id=article_id)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, article=article_data)
        return Response(serializer.data)