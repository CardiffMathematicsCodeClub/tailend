from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """View set for User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """View set for Player"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    """View set for Game"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
