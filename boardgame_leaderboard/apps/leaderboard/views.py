# Views are used to encapsulate logic for processing requests and returning responses.
# It's usually called a Controller, but Django is a little different.

from django.shortcuts import render
from .models import Boardgame
from .serializers import BoardgameSerializer
from rest_framework import generics

class BoardgameListCreate(generics.ListCreateAPIView):
    queryset = Boardgame.objects.all()
    serializer_class = BoardgameSerializer

    
