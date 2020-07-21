from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from faker import Factory
from .. import models


""" URLS for tests """
BOARDGAME_URL = reverse('leaderboard:boardgame-list')
PLAYER_URL = reverse('leaderboard:player-list')



class BoardgameTests(APITestCase):
    
    def test_create_boardgame(self):
        """
        Tests for successful creation of a boardgame
        """
        url = BOARDGAME_URL
        data = {'name':'test_boardgame', 'genre':'strategy', 'max_players':'6'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Boardgame.objects.count(), 1)
        self.assertEqual(models.Boardgame.objects.get().name, 'test_boardgame')
        self.assertEqual(models.Boardgame.objects.get().genre, 'strategy')

class PlayerTests(APITestCase):
    
    def test_create_player(self):
        """
        Tests for successful creation of a player
        """
        url = PLAYER_URL
        data = {'name':'eggbert'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Player.objects.count(), 1)
        self.assertEqual(models.Player.objects.get().name, 'eggbert')


# class PlayerSetTests(APITestCase):

#     def set_up(self):


