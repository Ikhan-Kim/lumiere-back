from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, ArticleComment


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'user']

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleDetailSerializer(serializers.ModelSerializer):
    comments = ArticleCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'