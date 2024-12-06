from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ArticleViewSet

api_router = routers.DefaultRouter()
api_router.register('articles', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]