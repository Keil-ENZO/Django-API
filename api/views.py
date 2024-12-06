from rest_framework import viewsets
from api.serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(article__id = self.kwargs['article_pk'])

