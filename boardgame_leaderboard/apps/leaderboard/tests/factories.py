import factory
from faker import Factory
from random import choice
from .. import models

# Factory to use for creation
faker = Factory.create()

class BoardgameFactory(factory.DjangoModelFactory):
    """
    Factory to create fake boardgames for testing
    """
    class Meta:
        model = models.Boardgame

    name = factory.Sequence((lambda n: 'Boardgame_{}'.format(n)))
    genre = models.get_random_genre()
    created_at = factory.LazyAttribute(lambda _: faker.date())


class PlayerFactory(factory.DjangoModelFactory):
    """
    Factory to create fake players for testing
    """
    class Meta:
        model = models.Player 
    
    name = factory.LazyAttribute(lambda _: faker.name())
    created_at = factory.LazyAttribute(lambda _: faker.date())


class PlayerSetFactory(factory.DjangoModelFactory):
    """
    Factory to create fake player sets for testing
    """
    class Meta:
        model = models.PlayerSet

    name = factory.Sequence((lambda n: 'Playerset_{}'.format(n)))
    
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
    
    created_at = factory.LazyAttribute(lambda _: faker.date())

class GameFactory(factory.DjangoModelFactory):
    """
    Factory to create fake games for testing
    Does not assign a winner.
    """
    class Meta:
        model = models.Game

    boardgame = factory.SubFactory(BoardgameFactory)
    player_set = factory.SubFactory(PlayerSetFactory)

    created_at = factory.LazyAttribute(lambda _: faker.date())

    
    


