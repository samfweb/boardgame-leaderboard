from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creates a router to automatically generate url patterns
router = DefaultRouter()
router.register(r'genres', views.GenreViewSet, 'genres')
router.register(r'boardgames', views.BoardgameViewSet, 'boardgames')
router.register(r'players', views.PlayerViewSet, 'players')
router.register(r'games', views.GameViewSet, 'games')
router.register(r'playergamedatas', views.PlayerGameDataViewSet, 'playergamedatas')

urlpatterns = [
    path('', include((router.urls, 'leaderboard'))),
]