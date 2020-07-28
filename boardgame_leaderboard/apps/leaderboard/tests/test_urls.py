from django.urls import reverse

BOARDGAME_URL   = reverse('leaderboard:boardgame-list'),
PLAYER_URL      = reverse('leaderboard:player-list'),
PLAYER_SET_URL  = reverse('leaderboard:playerset-list'),
GAME_UR         = reverse('leaderboard:game-list')

