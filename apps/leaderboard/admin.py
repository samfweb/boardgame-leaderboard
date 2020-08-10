from django.contrib import admin
from .models import Genre, Boardgame, Game, Player, PlayerGameData

admin.site.register(Genre)
admin.site.register(Boardgame)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerGameData)

