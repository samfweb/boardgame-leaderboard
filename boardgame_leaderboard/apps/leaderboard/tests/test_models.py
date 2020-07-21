from django.test import TestCase
from .. import models

class ModelTests(TestCase):

    def test_get_random_genre(self):
        genre_set = set()
        for genre_tuple in models.GAME_GENRES:
            genre_set.add(genre_tuple[0])
        self.assertIn(models.get_random_genre(), genre_set)