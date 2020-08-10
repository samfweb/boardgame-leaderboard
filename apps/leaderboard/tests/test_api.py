from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, override_settings
from collections import OrderedDict
from .factories import *
from .test_urls import BOARDGAME_URL, PLAYER_URL, GAME_URL
from .. import models
import json, random


class BoardgameTests(APITestCase):
    
    def setUp(self):
        # Generate a list of random genres
        with override_settings(USE_TZ=False):
            self.fake_genres = GenreFactory.create_batch(10)
    
    def test_create_boardgame(self):
        """
        Tests for successful creation of a boardgame
        """
        name = faker.name()
        genre_name = random.choice(self.fake_genres).name
        max_players = str(random.choice(range(2,10)))

        url = reverse(BOARDGAME_URL)
        data = {'name':name, 
                'max_players':max_players, 
                'genres': [
                    {'name': genre_name}
                ]}        
        
        # Send post request
        response = self.client.post(url, data, format='json')

        # Check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Work out ID of new boardgame
        boardgame_id = models.Boardgame.objects.count()
        
        # Check db matches request
        self.assertEqual(models.Boardgame.objects.get(pk=boardgame_id).name, name)
        self.assertEqual(models.Boardgame.objects.get(pk=boardgame_id).genres[0]['name'], genre_name)
        
        # Max players is an int, so convert to string for comparing
        self.assertEqual(str(models.Boardgame.objects.get(pk=boardgame_id).max_players), max_players)


class PlayerTests(APITestCase):
    
    def test_create_player(self):
        """
        Tests for successful creation of a player
        """
        name = factory.LazyAttribute(lambda _: faker.name())
        url = reverse(PLAYER_URL)
        data = {'name':name}
        
        # Send a post request
        response = self.client.post(url, data, format='json')

        # Check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Work out ID of new player
        player_id = models.Player.objects.count()

        # Check database
        self.assertEqual(models.Player.objects.get(pk=player_id).name, name)


class GameTests(APITestCase):

    def setUp(self):
        with override_settings(USE_TZ=False):
            self.boardgame = BoardgameFactory()

    def test_create_game(self):
        
        data = {
            'boardgame':self.boardgame.id, 
        }

        response = self.client.post(url, data, format='json')

        # Check game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PlayerGameDataTests(APITestCase):

    def setUp(self):
        pass
    
    def test_add_duplicate_player(self):
        pass

    def test_add_too_many_scores(self):
        pass

    def test_patch_score(self):
        pass

    def test_delete_score(self):
        pass


    






# class PlayerSetTests(APITestCase):

#     def create_player_set_post_data(self, players):
#         """
#         Creates a json payload for the creation of a player set
        
#         Args:
#             players : a list of <Player> database objects

#         Returns:
#             An ordered dict with json data 
#         """
#         data = OrderedDict()
#         data['name'] = 'Test_Player_Set'

#         player_key = 'player'
#         i = 0
#         for i in range(10):
#             # make key of form "player#"
#             key = player_key + str(i+1)

#             if i < len(players):
#                 # Add the player to data
#                 data[key] = str(players[i].id)
        
#         return data

#     def post_player_set(self, player_set):
#         """
#         Posts a set of players to the database

#         Args:
#             player_set ([<Player Object>]): list of created player objects

#         Returns:
#             A Django response object
#         """
        
#         # Get URL to post to
#         url = reverse(PLAYER_SET_URL)

#         # Generate JSON data
#         data = self.create_player_set_post_data(player_set)
        
#         # Send a post request
#         response = self.client.post(url, data, format='json')

#         return response
    

#     def test_create_full_player_set(self):
#         """
#         Tests for successful creation of a full player set
#         """
#         # Stop warnings that faker's date is naive
#         with override_settings(USE_TZ=False):
#             players = PlayerFactory.create_batch(10)

#         response = self.post_player_set(players)

#         # Check response
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    

#     def test_create_partial_player_set(self):
#         """
#         Tests for successful creation of player sets with < 10 members
#         """
#         for i in range(1,10):
#             # Stop warnings that faker's date is naive
#             with override_settings(USE_TZ=False):
#                 players = PlayerFactory.create_batch(10)
            
#             response = self.post_player_set(players)

#             # Check response
#             self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#     def test_player_set_with_duplicate_player(self):
#         """
#         Tests unique player requirement in player set
#         """
#         # Count player sets
#         count = models.PlayerSet.objects.count()

#         # Stop warnings that faker's date is naive
#         with override_settings(USE_TZ=False):
#             players = PlayerFactory.create_batch(3)
        
#         # Repeat one of the players
#         players.append(players[2])

#         # Generate JSON data
#         response = self.post_player_set(players)

#         # Check response doesn't pass validation
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#         # Check no player sets have been created
#         self.assertEqual(count, models.PlayerSet.objects.count())

                
        
        


