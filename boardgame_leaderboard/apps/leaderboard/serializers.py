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
        print("-------------------------")
        print(genres_data)
        boardgame = Boardgame.objects.create(**validated_data)
        
        for genre in genres_data:
            print(genre)
            obj = Genre.objects.get(name=genre['name'])
            #obj, created = Genre.objects.get_or_create(name=genre['name'])
            print(obj)
            boardgame.genres.add(obj)
        return boardgame

    def update(self, instance, validated_data):
        print("Update Called-------------------------")
        genres_data = validated_data.pop('genres')

        # Update boardgame 
        instance.name = validated_data.get('name', instance.name)
        instance.max_players = validated_data.get('max_players', instance.max_players) 
    
        for genre in genres_data:
            print(genre)
            obj, created = Genre.objects.get_or_create(name=genre['name'])
            print(obj)
            instance.genres.add(obj)
        
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