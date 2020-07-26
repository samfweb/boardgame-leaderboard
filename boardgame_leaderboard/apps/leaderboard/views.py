# Views are used to encapsulate logic for processing requests and returning responses.
# It's usually called a Controller, but Django is a little different.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Boardgame, Player, PlayerSet, Game
from .serializers import BoardgameSerializer, PlayerSerializer, PlayerSetSerializer, GameSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Custom functions
# ----------------

def test_redirect(response):
    response = redirect('/api/leaderboard')
    return response



# Standard API viewsets
# ---------------------

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

    # @action(methods=['put'], detail=True)
    # def partial_update(self, request, pk=None):
    #     game = self.get_object()
    #     serializer = GameSerializer(data=request.data, partial=True)
    #     if serializer.is_valid():
    #         # Checks to see whether the winner being set is valid
    #         result = game.set_winner(serializer.data['winner'])
    #         if result == Game.WINNER_SET:
    #             game.save()
    #             return Response({'status': 'winner set'},
    #                                 status=status.HTTP_202_ACCEPTED)

    #         # The Player is not in the Game's player_set
    #         elif result == Game.NOT_IN_PLAYER_SET:
    #             return Response({'player_id error':'player not in set'}, 
    #                                 status=status.HTTP_304_NOT_MODIFIED)

    #         # The Player does not exist
    #         else:
    #             return Response({'player_id error':'player does not exist'},
    #                                 status=status.HTTP_304_NOT_MODIFIED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    
