from django.urls import path
from . import views


urlpatterns = [
    path('api/leaderboard/boardgames', views.BoardgameListCreate.as_view() ),
    path('api/leaderboard/players', views.PlayerListCreate.as_view() ),
    path('api/leaderboard/playersets', views.PlayerSetListCreate.as_view() ),
    path('api/leaderboard/games', views.GameListCreate.as_view() ),
]