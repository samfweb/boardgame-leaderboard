from rest_framework import serializers
from .models import Boardgame, Player, PlayerSet, Game
from django.core.exceptions import ValidationError
import logging


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

    def validate(self, data):
        """
        Check that all players are unique
        """
        players = set()
        for key, value in data.items():
            if 'player' in key and value != None:
                # Check if the player has already been encountered
                if value in players:
                    raise serializers.ValidationError("Player " + str(value) + " is already in the set.")
                # If not, add it to the set
                players.add(value)
        return data


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'boardgame', 'player_set', 'winner',)


    def validate_winner(self, value):
        """
        Check that the winner is in the game's player_sets or is null
        """
        data = self.get_initial()
        player_ids = (PlayerSet.objects.get(id=data['player_set'])).get_players_in_set(keyword='ids')
        
        if str(data['winner']) not in player_ids:
            raise serializers.ValidationError("Winner is not one of the game's players")
        return value
        # PlayerSet.objects.get(data['player_set']).get_players_in_set(keyword='ids')