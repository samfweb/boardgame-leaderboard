from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
import random 



class Genre(models.Model):

    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)



class Boardgame(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
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


class PlayerGameData(models.Model):
    
    player = models.ForeignKey(Player, related_name='%(class)s_player', on_delete=models.PROTECT)
    game = models.ForeignKey(Game, related_name='%(class)s_game', on_delete=models.PROTECT)
    score = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('player', 'game')


# # Note for later: a PlayerSet Manager needs to be created for any table-wide operations    
# class PlayerSet(models.Model):
#     name = models.CharField(max_length=100, default='New PlayerSet')
#     player1  = models.ForeignKey(Player, related_name='%(class)s_p1',  on_delete=models.PROTECT)
#     player2  = models.ForeignKey(Player, related_name='%(class)s_p2',  on_delete=models.PROTECT, null='True')
#     player3  = models.ForeignKey(Player, related_name='%(class)s_p3',  on_delete=models.PROTECT, null='True')
#     player4  = models.ForeignKey(Player, related_name='%(class)s_p4',  on_delete=models.PROTECT, null='True')
#     player5  = models.ForeignKey(Player, related_name='%(class)s_p5',  on_delete=models.PROTECT, null='True')
#     player6  = models.ForeignKey(Player, related_name='%(class)s_p6',  on_delete=models.PROTECT, null='True')
#     player7  = models.ForeignKey(Player, related_name='%(class)s_p7',  on_delete=models.PROTECT, null='True')
#     player8  = models.ForeignKey(Player, related_name='%(class)s_p8',  on_delete=models.PROTECT, null='True')
#     player9  = models.ForeignKey(Player, related_name='%(class)s_p9',  on_delete=models.PROTECT, null='True')
#     player10 = models.ForeignKey(Player, related_name='%(class)s_p10', on_delete=models.PROTECT, null='True')
#     created_at = models.DateTimeField(default=timezone.now)


#     def get_players_in_set(self, keyword='default'):
#         """ Gets a list of all (player#, player_id) tuples in the PlayerSet """
#         # Gets a list of all (player#, player_id) tuples in the PlayerSet
#         player_tuples = [(field.name, field.value_to_string(self)) \
#             for field in PlayerSet._meta.fields if 'player' in field.name]

#         if keyword != 'names' and keyword != 'ids':
#             return player_tuples

#         # Return a list of either names or ids
#         else:
#             players_list = []
#             for (player_number, player_id) in player_tuples:
#                 if player_id != 'None':
#                     # Return a list of all names
#                     if keyword == 'names':
#                         players_list.append(" " + (Player.objects.get(id=player_id).name))
#                     # Return a list of all ids
#                     else:
#                         players_list.append(player_id)
#         return players_list

#     def __str__(self):
#         """ 
#         String is of form: 
#         PlayerSet Name: player1 player2...playern 
#         """
#         str_rep = self.name + ":"
#         for player_name in self.get_players_in_set(keyword='names'):
#             str_rep += " " + player_name
#         return str_rep
