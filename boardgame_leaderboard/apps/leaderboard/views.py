# Views are used to encapsulate logic for processing requests and returning responses.
# It's usually called a Controller, but Django is a little different.

from django.shortcuts import render
from .models import Boardgame, Player, PlayerSet, Game
from .serializers import BoardgameSerializer, PlayerSerializer, PlayerSetSerializer, GameSerializer
from rest_framework import generics

class BoardgameListCreate(generics.ListCreateAPIView):
    queryset = Boardgame.objects.all()
    serializer_class = BoardgameSerializer

class PlayerListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerSetListCreate(generics.ListCreateAPIView):
    queryset = PlayerSet.objects.all()
    serializer_class = PlayerSetSerializer

class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
