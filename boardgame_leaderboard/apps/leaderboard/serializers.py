from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Genre, Boardgame, Player, Game, PlayerGameData


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

    def __str__(self):
        return self.name


class BoardgameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardgame
        fields = ('id', 'name', 'max_players', 'genres')

    # Have to define custom create and update once genres isn't read_only
    # def create(self, validated_data):
    #     genres_data = validated_data.pop('genres')
    #     boardgame = Boardgame.objects.create(**validated_data)
    #     for grenre_data in genres_data:

        
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'boardgame')


class PlayerGameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerGameData
        fields = ('id', 'player', 'game', 'score')
    


# ------------------
# Validation example:

    # def validate_winner(self, value):
    #     """
    #     Check that the winner is in the game's players or is null
    #     """
    #     # data = self.get_initial()
    #     # player_ids = (PlayerSet.objects.get(id=data['player_set'])).get_players_in_set(keyword='ids')
        
    #     # if str(data['winner']) not in player_ids:
    #     #     raise serializers.ValidationError("Winner is not one of the game's players")
    #     return value