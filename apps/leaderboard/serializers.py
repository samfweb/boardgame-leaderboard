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
    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Boardgame
        fields = ('id', 'name', 'max_players', 'genres')

    # Have to define custom create and update due to nested serializer
    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        boardgame = Boardgame.objects.create(**validated_data)
        
        for genre in genres_data:
            obj, created = Genre.objects.get_or_create(name=genre['name'])
            boardgame.genres.add(obj)

        return boardgame

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genres')

        # Update boardgame 
        instance.name = validated_data.get('name', instance.name)
        instance.max_players = validated_data.get('max_players', instance.max_players) 

        # Remove all genres from boardgame
        instance.genres.clear()

        # Create Genre if new, and add it to genre list
        for genre in genres_data:
            obj, created = Genre.objects.get_or_create(name=genre['name'])
            instance.genres.add(obj)
        
        instance.save()

        return instance


        
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

    # Custom create to ensure max player count hasn't been exceeded for a game
    def create(self, validated_data):
        game = validated_data['game']
        curr_players = game.players.all().count()
        max_players = game.boardgame.max_players

        print(f"Current players: {curr_players}, max players: {max_players}")

        if curr_players >= max_players:
            raise ValidationError(
                ('Maximum player count for game %(game_id)s (%(max_players)s) has been reached'),
                params={'game_id': game.id, 'max_players': max_players},
            )

        player_game_data = PlayerGameData.objects.create(**validated_data)

        return player_game_data
    


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