import factory, random
from faker import Factory
from .. import models

# Factory to use for creation
faker = Factory.create()

class GenreFactory(factory.DjangoModelFactory):
    """
    Factory to create fake genres for testing
    """
    class Meta:
        model = models.Genre

    name = factory.Sequence((lambda n: 'Boardgame_{}'.format(n)))
    created_at = factory.LazyAttribute(lambda _: faker.date())


class BoardgameFactory(factory.DjangoModelFactory):
    """
    Factory to create fake boardgames for testing
    """
    class Meta:
        model = models.Boardgame

    name = factory.Sequence((lambda n: 'Boardgame_{}'.format(n)))
    genre = factory.SubFactory(GenreFactory)
    created_at = factory.LazyAttribute(lambda _: faker.date())


class PlayerFactory(factory.DjangoModelFactory):
    """
    Factory to create fake players for testing
    """
    class Meta:
        model = models.Player 
    
    name = factory.LazyAttribute(lambda _: faker.name())
    created_at = factory.LazyAttribute(lambda _: faker.date())


class GameFactory(factory.DjangoModelFactory):
    """
    Factory to create fake games for testing
    """
    class Meta:
        model = models.Game

    boardgame = factory.SubFactory(BoardgameFactory)
    created_at = factory.LazyAttribute(lambda _: faker.date())


class PlayerGameDataFactory(factory.DjangoModelFactory):
    """
    Factory to create fake PlayerGameData for testing
    """
    class Meta:
        model = models.PlayerGameData

    player = factory.SubFactory(PlayerFactory)
    game = factory.SubFactory(BoardgameFactory)
    score = random.choice(range(1001))
    created_at = factory.LazyAttribute(lambda _: faker.date())
    

