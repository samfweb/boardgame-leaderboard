from django.test import TestCase
from .. import models
from .test_urls import *

class ModelTests(TestCase):

    def test_get_random_genre(self):
        genre_set = set()
        for (genre_slug, genre_verbose) in models.Boardgame.GAME_GENRES:
            # Add the genre's slug to the set
            genre_set.add(genre_slug)
        self.assertIn(models.get_random_genre(), genre_set)

# class BoardgameTests(TestCase):

#     def setUp(self):
#         self.
