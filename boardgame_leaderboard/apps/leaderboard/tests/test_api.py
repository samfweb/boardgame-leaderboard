from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .factories import *
from .test_urls import *
from .. import models


class BoardgameTests(APITestCase):
    
    def test_create_boardgame(self, name='default_name', genre='strategy', max_players='6'):
        """
        Tests for successful creation of a boardgame
        Optional arguments:
            name
            genre
            max_players
        """
        url = BOARDGAME_URL
        data = {'name':name, 'genre':genre, 'max_players':max_players}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Boardgame.objects.count(), 1)
        self.assertEqual(models.Boardgame.objects.get().name, name)
        self.assertEqual(models.Boardgame.objects.get().genre, genre)
        self.assertEqual(models.Boardgame.objects.get().max_players, max_players)


class PlayerTests(APITestCase):
    
    def test_create_player(self, name='default name'):
        """
        Tests for successful creation of a player
        Optional arguments:
            name
        """
        url = PLAYER_URL
        data = {'name':name}
        
        # Send a post request
        response = self.client.post(url, data, format='json')

        # Check database matches
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Player.objects.count(), 1)
        self.assertEqual(models.Player.objects.get().name, name)


# class PlayerSetTests(APITestCase):

#     def test_create_player_set():



#     def test_player_set_with_duplicate_player()
        
        


