from rest_framework import routers
from api.views import ArticleViewSet

api_router = routers.DefaultRouter()
api_router.register('articles', ArticleViewSet)