import factory
from faker import Factory
from .. import models

faker = Factory.create()

class BoardgameFactory(factory.DjangoModelFactory):
    class Meta:
        model = Boardgame
    name = faker.name()
    genre = models.get_random_genre()
    
    


