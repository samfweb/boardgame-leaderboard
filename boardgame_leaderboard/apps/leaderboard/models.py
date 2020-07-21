from django.db import models
from django.utils import timezone 


class Boardgame(models.Model):
    GAME_GENRES = (
        ('strategy', 'Strategy'),
        ('deckbuilding', 'Deckbuilding'),
        ('rpg', 'RPG'),
        ('coop', 'Co-op')
    )
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GAME_GENRES)
    max_players = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Note for later: a PlayerSet Manager needs to be created for any table-wide operations    
class PlayerSet(models.Model):
    name = models.CharField(max_length=100, default='New PlayerSet')
    player1 = models.ForeignKey(Player, related_name='%(class)s_p1', on_delete=models.PROTECT)
    player2 = models.ForeignKey(Player, related_name='%(class)s_p2', on_delete=models.PROTECT, null='True')
    player3 = models.ForeignKey(Player, related_name='%(class)s_p3', on_delete=models.PROTECT, null='True')
    player4 = models.ForeignKey(Player, related_name='%(class)s_p4', on_delete=models.PROTECT, null='True')
    player5 = models.ForeignKey(Player, related_name='%(class)s_p5', on_delete=models.PROTECT, null='True')
    player6 = models.ForeignKey(Player, related_name='%(class)s_p6', on_delete=models.PROTECT, null='True')
    player7 = models.ForeignKey(Player, related_name='%(class)s_p7', on_delete=models.PROTECT, null='True')
    player8 = models.ForeignKey(Player, related_name='%(class)s_p8', on_delete=models.PROTECT, null='True')
    player9 = models.ForeignKey(Player, related_name='%(class)s_p9', on_delete=models.PROTECT, null='True')
    player10 = models.ForeignKey(Player, related_name='%(class)s_p10', on_delete=models.PROTECT, null='True')
    created_at = models.DateTimeField(default=timezone.now)

    def get_players_in_set(self):
        """ Gets a list of all (player#, player_id) tuples in the PlayerSet """
        return [(field.name, field.value_to_string(self)) \
            for field in PlayerSet._meta.fields if 'player' in field.name]

    def get_players_names_in_set(self):
        """ Gets a list of all Player.names in the PlayerSet """
        players_names = []
        for player in self.get_players_in_set():
            if player[1] != 'None':
                players_names.append(" " + str(Player.objects.get(id=player[1])))
        return players_names

    def __str__(self):
        """ String is of form: 
        PlayerSet Name: player1 player2...playern 
        """
        str_rep = self.name + ":"
        for player_name in self.get_players_names_in_set():
            str_rep += " " + player_name
        return str_rep

class Game(models.Model):
    boardgame = models.ForeignKey(Boardgame, related_name='%(class)s_boardgame', on_delete=models.PROTECT)
    players = models.ForeignKey(PlayerSet, related_name='%(class)s_playerset', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    winner = models.ForeignKey(
        Player, 
        related_name='%(class)s_winner', 
        # limit_choices_to={self.players.get_players_in_set(self)},
        on_delete=models.PROTECT,
        null=True,)

    def __str__(self):
        return (self.boardgame + ", " + self.date + ", Winner:" + self.winner)
