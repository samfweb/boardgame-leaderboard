import factory
from faker import Factory
from random import choice
from .. import models

# Factory to use for creation
faker = Factory.create()

@factory.lazy_attribute
class BoardgameFactory(factory.DjangoModelFactory):
    """
    Factory to create fake boardgames for testing
    """
    class Meta:
        model = models.Boardgame

    name = faker.word()
    genre = models.get_random_genre()


class PlayerFactory(factory.DjangoModelFactory):
    """
    Factory to create fake players for testing
    """
    class Meta:
        model = models.Player 
    
    name = faker.name()


class PlayerSetFactory(factory.DjangoModelFactory):
    """
    Factory to create fake player sets for testing
    """
    class Meta:
        model = models.PlayerSet

    name = faker.name() + "'s Player Set"
    
    # Use PlayerFactory to create players
    player1 = factory.SubFactory(PlayerFactory)
    player2 = factory.SubFactory(PlayerFactory) 
    player3 = factory.SubFactory(PlayerFactory)
    player4 = factory.SubFactory(PlayerFactory)
    player5 = factory.SubFactory(PlayerFactory)
    player6 = factory.SubFactory(PlayerFactory)
    player7 = factory.SubFactory(PlayerFactory)
    player8 = factory.SubFactory(PlayerFactory)
    player9 = factory.SubFactory(PlayerFactory)
    player10 = factory.SubFactory(PlayerFactory)
    
    created_at = faker.date()


class GameFactory(factory.DjangoModelFactory):
    """
    Factory to create fake games for testing
    """
    class Meta:
        model = models.Game

    # Use PlayerSetFactory to create a Player Set
    player_set = factory.SubFactory(PlayerSetFactory) 

    # Choose winner as first player
    # winner = player_set.player1
    print(player_set)

    created_at = faker.date()

    
    


