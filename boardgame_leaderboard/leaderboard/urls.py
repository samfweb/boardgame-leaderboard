from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="leaderboard-home"),
    path('about/', views.about, name="leaderboard-about"),
]