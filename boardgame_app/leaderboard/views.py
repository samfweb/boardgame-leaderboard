from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Leaderboard Home</h1>")


def about(request):
    return HttpResponse("<h2>This is a boardgame leaderboard for Jenny and meeeeee</h2>")

