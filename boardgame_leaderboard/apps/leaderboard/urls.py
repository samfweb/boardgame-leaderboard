from django.urls import path
from . import views

urlpatterns = [
    path('api/leaderboard/', views.BoardgameListCreate.as_view() ),
]