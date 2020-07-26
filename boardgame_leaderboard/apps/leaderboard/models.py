from django.db import models
from django.utils import timezone
import random 




def get_random_genre():
    """
    Gets a random genre from the list
    """
    return random.choice(Boardgame.GAME_GENRES)[0]

class Boardgame(models.Model):

    # May need to create a model for these in later versions
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
        return "ID:" + str(self.id) + " " + self.name

# Note for later: a PlayerSet Manager needs to be created for any table-wide operations    
class PlayerSet(models.Model):
    name = models.CharField(max_length=100, default='New PlayerSet')
    player1  = models.ForeignKey(Player, related_name='%(class)s_p1',  on_delete=models.PROTECT)
    player2  = models.ForeignKey(Player, related_name='%(class)s_p2',  on_delete=models.PROTECT, null='True')
    player3  = models.ForeignKey(Player, related_name='%(class)s_p3',  on_delete=models.PROTECT, null='True')
    player4  = models.ForeignKey(Player, related_name='%(class)s_p4',  on_delete=models.PROTECT, null='True')
    player5  = models.ForeignKey(Player, related_name='%(class)s_p5',  on_delete=models.PROTECT, null='True')
    player6  = models.ForeignKey(Player, related_name='%(class)s_p6',  on_delete=models.PROTECT, null='True')
    player7  = models.ForeignKey(Player, related_name='%(class)s_p7',  on_delete=models.PROTECT, null='True')
    player8  = models.ForeignKey(Player, related_name='%(class)s_p8',  on_delete=models.PROTECT, null='True')
    player9  = models.ForeignKey(Player, related_name='%(class)s_p9',  on_delete=models.PROTECT, null='True')
    player10 = models.ForeignKey(Player, related_name='%(class)s_p10', on_delete=models.PROTECT, null='True')
    created_at = models.DateTimeField(default=timezone.now)


    def get_players_in_set(self, keyword='default'):
        """ Gets a list of all (player#, player_id) tuples in the PlayerSet """
        # Gets a list of all (player#, player_id) tuples in the PlayerSet
        player_tuples = [(field.name, field.value_to_string(self)) \
            for field in PlayerSet._meta.fields if 'player' in field.name]

        if keyword != 'names' and keyword != 'ids':
            return player_tuples

        # Return a list of either names or ids
        else:
            players_list = []
            for (player_number, player_id) in player_tuples:
                if player_id != 'None':
                    # Return a list of all names
                    if keyword == 'names':
                        players_list.append(" " + (Player.objects.get(id=player_id).name))
                    # Return a list of all ids
                    else:
                        players_list.append(player_id)
        return players_list

    def __str__(self):
        """ 
        String is of form: 
        PlayerSet Name: player1 player2...playern 
        """
        str_rep = self.name + ":"
        for player_name in self.get_players_in_set(keyword='names'):
            str_rep += " " + player_name
        return str_rep

class Game(models.Model):

    boardgame = models.ForeignKey(Boardgame, related_name='%(class)s_boardgame', on_delete=models.PROTECT)
    player_set = models.ForeignKey(PlayerSet, related_name='%(class)s_playerset', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    winner = models.ForeignKey(Player, related_name='%(class)s_winner', on_delete=models.PROTECT, null=True)