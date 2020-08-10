from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from .validators import validate_unique_genre, validate_unique_boardgame
import random 


class Genre(models.Model):

    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)



class Boardgame(models.Model):
    
    name = models.CharField(max_length=100)
    max_players = models.IntegerField(validators=[MinValueValidator(1)])
    genres = models.ManyToManyField(Genre, related_name="genre_list", default=None)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ID:" + str(self.id) + " " + self.name


class Game(models.Model):

    boardgame = models.ForeignKey(Boardgame, related_name='%(class)s_boardgame', on_delete=models.PROTECT)
    players = models.ManyToManyField(Player, through='PlayerGameData')
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def get_player_count(self):
        return len(self.players)


class PlayerGameData(models.Model):
    
    player = models.ForeignKey(Player, related_name='%(class)s_player', on_delete=models.PROTECT)
    game = models.ForeignKey(Game, related_name='%(class)s_game', on_delete=models.PROTECT)
    score = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('player', 'game')
