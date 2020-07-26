from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creates a router to automatically generate url patterns
router = DefaultRouter()
router.register(r'boardgames', views.BoardgameViewSet, 'boardgame')
router.register(r'players', views.PlayerViewSet, 'player')
router.register(r'playersets', views.PlayerSetViewSet, 'playerset')
router.register(r'games', views.GameViewSet, 'game')

urlpatterns = [
    path('api/leaderboard/', include((router.urls, 'leaderboard'), namespace='api')),
    path('', views.test_redirect),
]