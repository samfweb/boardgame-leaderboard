# Views are used to encapsulate logic for processing requests and returning responses.
# It's usually called a Controller, but Django is a little different.

import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize 
from .models import Genre, Boardgame, Player, Game, PlayerGameData
from .serializers import GenreSerializer, BoardgameSerializer, PlayerSerializer, \
                            GameSerializer, PlayerGameDataSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Custom functions
# ----------------

def root_redirect(response):
    response = redirect('/api/leaderboard')
    return response


def create_response(models):
    """
    Creates a django response object from a queryset
    Args:
        models (queryset): List of django models.

    Returns:
        Django response object: The response in JSON format.
    """
    # Serialise the list of models into a JSON string
    str_data = serialize('json', models)

    # Convert this into JSON
    data = json.loads(str_data)

    # Create a response
    return Response(data=data)



# Standard API viewsets
# ---------------------

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # /api/leaderboard/genres/<pk>/boardgames
    @action(methods=['get'], detail=True, url_path='boardgames', url_name='genre_boardgames')
    def get_boardgames(self, request, pk=None):
        """
        Queries the db for the boardgames of a genre
        Args:
            request (django-rest-framework request object): The request.
            pk (int, optional): The genre's boardgames to return. Defaults to None.

        Returns:
            Django response object: The response in JSON format.
        """
        # Gets the genre being queried
        genre = self.get_object()

        # Queries the database for boardgames that have this genre
        boardgames = Boardgame.objects.filter(genres__in=[genre.id])

        return create_response(boardgames)


class BoardgameViewSet(viewsets.ModelViewSet):
    queryset = Boardgame.objects.all()
    serializer_class = BoardgameSerializer

    # /api/leaderboard/boardgames/<pk>/games
    @action(methods=['get'], detail=True, url_path='games', url_name='boardgame_games')
    def get_games(self, request, pk=None):
        """
        Queries the db for the games of a boardgame.
        """
        # Gets the genre being queried
        boardgame = self.get_object()

        # Queries the database for boardgames that have this genre
        games = Games.objects.filter(boardgame=boardgame.id)

        return create_response(games)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    # /api/leaderboard/players/<pk>/games
    @action(methods=['get'], detail=True, url_path='games', url_name='player_games')
    def player_games(self, request, pk=None):
        """
        Queries the db for the games of a player.
        """
        # Gets the game being queried
        player = self.get_object()

        # Queries the database for games that have been played by this player
        games = Game.objects.filter(players__id=player.id)

        return create_response(games)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # /api/leaderboard/games/<pk>/players
    @action(methods=['get'], detail=True, url_path='players', url_name='game_players')
    def game_players(self, request, pk=None):
        """
        Queries the db for the players of a game.
        """
        # Gets the game being queried
        game = self.get_object()

        # Queries the database for players that have been added to this game
        players = Player.objects.filter(game__id=game.id)

        return create_response(players)

    # /api/leaderboard/games/<pk/scores
    @action(methods=['get'], detail=True, url_path='scores', url_name='game_scores')
    def game_scores(self, request, pk=None):
        """
        Gets the scores for a game
        """
        # Gets the game being queried
        game = self.get_object()

        # Gets the scores in descending order
        player_game_datas = PlayerGameData.objects.filter(game__id=game.id).order_by('-score')

        return create_response(player_game_datas)

        
class PlayerGameDataViewSet(viewsets.ModelViewSet):
    queryset = PlayerGameData.objects.all()
    serializer_class = PlayerGameDataSerializer
        

    
    
