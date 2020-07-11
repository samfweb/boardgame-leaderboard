from django.db import models

class Boardgame(models.Model):
    GAME_GENRES = (
        ('strategy', 'Strategy'),
        ('deckbuilding', 'Deckbuilding'),
        ('rpg', 'RPG')
    )
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GAME_GENRES)
    max_players = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    boardgame = models.ForeignKey(Boardgame, related_name='%(class)s_boardgame', on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    winner = models.ForeignKey(Player, related_name='%(class)s_winner', on_delete=models.CASCADE)