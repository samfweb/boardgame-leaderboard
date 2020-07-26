# Views are used to encapsulate logic for processing requests and returning responses.
# It's usually called a Controller, but Django is a little different.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Boardgame, Player, PlayerSet, Game
from .serializers import BoardgameSerializer, PlayerSerializer, PlayerSetSerializer, GameSerializer
from rest_framework import viewsets

# Custom functions



# Standard API viewsets
class BoardgameViewSet(viewsets.ModelViewSet):
    queryset = Boardgame.objects.all()
    serializer_class = BoardgameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerSetViewSet(viewsets.ModelViewSet):
    queryset = PlayerSet.objects.all()
    serializer_class = PlayerSetSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
