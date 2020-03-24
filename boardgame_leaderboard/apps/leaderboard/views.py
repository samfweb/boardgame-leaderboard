from django.shortcuts import render
from django.http import HttpResponse
from apps.leaderboard import models

# Test games while I work our CSS
# games = [
#     {
#         'name': '7 Wonders Duel',
#         'players': '2',
#         'desc': 'We love it! Duel for the strongest military, science or culture.',
#         'last_updated': 'March 15, 2020',
#     }, 
#     {
#         'name': 'Splendour',
#         'players': '2-4',
#         'desc': 'Become the gem master',
#         'last_updated': 'March 15, 2020',
#     }
# ]




def home(request):
    games = models.get("boardgame")
    context = {
        'games': games
    }
    print()
    return render(request, 'leaderboard/home.html', context)


def about(request):
    return render(request, 'leaderboard/about.html')

