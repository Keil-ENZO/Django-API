from os.path import basename

from django.urls import path, include
from rest_framework import routers
from api.views import ArticleViewSet, CommentViewSet
from rest_framework_nested import routers

# api_router = routers.DefaultRouter()
api_router = routers.SimpleRouter()

api_router.register(r'articles', ArticleViewSet, basename='article')
articles_router = routers.NestedSimpleRouter(api_router, r'articles', lookup='article')
articles_router.register(r'comments', CommentViewSet, basename='articles-comments')

urlpatterns = [
    path('', include(api_router.urls)),
    path('', include(articles_router.urls)),
]

# api_router.register(r'comments', CommentViewSet, basename='comment')