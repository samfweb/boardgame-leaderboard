from django.contrib import admin
from .models import Boardgame, Game, Player, PlayerSet


admin.site.register(Boardgame)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerSet)