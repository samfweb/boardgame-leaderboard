import factory
from faker import Factory
from .. import models

faker = Factory.create()


class BoardgameFactory(factory.DjangoModelFactory):
    class Meta:
        model = Boardgame

    name = faker.name()
    genre = models.get_random_genre()


class PlayerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Player 
    
    name = faker.name()


class PlayerSetFactory(factory.DjangoModelFactory):
    class Meta:
        model = PlayerSet

    name = faker.name()
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
    


class GameFactory(factory.DjangoModelFactory):
    class Meta:
        model = Game 
    
    


