from rest_framework import viewsets
from api.serializers import ArticleSerializer
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer