from rest_framework import serializers
from .models import Boardgame, Player, Game

class BoardgameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardgame
        fields = ('id', 'name', 'genre', 'max_players')
        