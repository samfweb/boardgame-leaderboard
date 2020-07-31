from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creates a router to automatically generate url patterns
router = DefaultRouter()
router.register(r'genres', views.GenreViewSet, 'genre')
router.register(r'boardgames', views.BoardgameViewSet, 'boardgame')
router.register(r'players', views.PlayerViewSet, 'player')
router.register(r'games', views.GameViewSet, 'game')
router.register(r'playergamedatas', views.PlayerGameDataViewSet, 'playergamedata')

urlpatterns = [
    path('', include(router.urls)),
]