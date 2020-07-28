from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, override_settings
from collections import OrderedDict
from .factories import *
from .test_urls import BOARDGAME_URL, PLAYER_URL, PLAYER_SET_URL, GAME_URL
from .. import models
import json


class BoardgameTests(APITestCase):
    
    def test_create_boardgame(self, id='100', name='default_name', genre='strategy', max_players='6'):
        """
        Tests for successful creation of a boardgame
        Optional arguments:
            name
            genre
            max_players
        """
        
        url = reverse(BOARDGAME_URL)
        data = {'name':name, 'genre':genre, 'max_players':max_players}        
        
        # Send post request
        response = self.client.post(url, data, format='json')

        # Check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Work out ID of new boardgame
        boardgame_id = models.Boardgame.objects.count()
        
        # Check db matches request
        self.assertEqual(models.Boardgame.objects.get(pk=boardgame_id).name, name)
        self.assertEqual(models.Boardgame.objects.get(pk=boardgame_id).genre, genre)
        
        # Max players is an int, so convert to strong for comparing
        self.assertEqual(str(models.Boardgame.objects.get(pk=boardgame_id).max_players), max_players)


class PlayerTests(APITestCase):
    
    def test_create_player(self, name='default name'):
        """
        Tests for successful creation of a player
        Optional arguments:
            name
        """
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

        # Check API


class PlayerSetTests(APITestCase):

    def create_player_set_post_data(self, players):
        """
        Creates a json payload for the creation of a player set
        Arguments:
            players : a list of <Player> database objects
        
        (Use PlayerFactory to generate this list easily)
        """
        data = OrderedDict()
        data['name'] = 'Test_Player_Set'

        player_key = 'player'
        i = 0
        for player in players:
            # Update the playerkey
            i += 1
            if i > 10:
                raise ValueError("Too many players")
            
            # Add the player to data
            key = player_key + str(i)
            data[key] = str(player.id)
        
        return data

    def create_player_set(self, num_players):
        """
        Creates a set of players using a post request.
        Asserts the creation was successful.
        Arguments:
            num_players : the number of players in the set
        """
        # Count the number of player sets in the database
        count = models.PlayerSet.objects.count()

        # Stop warnings that faker's date is naive
        with override_settings(USE_TZ=False):
            players = PlayerFactory.create_batch(num_players)

        # Get URL to post to
        url = reverse(PLAYER_SET_URL)
        print(url)
        
        # Generate JSON data
        data = self.create_player_set_post_data(players)

        # Send a post request
        response = self.client.post(url, data, format='json')

        # Check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check one player set has been created
        self.assertEqual(count + 1, models.PlayerSet.objects.count())

    
    def test_create_full_player_set(self):
        """
        Tests for successful creation of a full player set
        """
        self.create_player_set(10)
    

    def test_create_partial_player_set(self):
        """
        Tests for successful creation of a player set with < 10 members
        """
        for i in range(10):
            self.create_player_set(i)

#     def test_player_set_with_duplicate_player():

        
        


