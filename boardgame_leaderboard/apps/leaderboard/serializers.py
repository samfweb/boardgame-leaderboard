from rest_framework import serializers
from .models import Boardgame, Player, PlayerSet, Game


class BoardgameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardgame
        fields = ('id', 'name', 'genre', 'max_players')
        
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name')

class PlayerSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSet
        fields = ( 
            'id',
            'name',
            'player1', 
            'player2',
            'player3',
            'player4',
            'player5',
            'player6',
            'player7',
            'player8',
            'player9',
            'player10',)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'boardgame', 'players',)