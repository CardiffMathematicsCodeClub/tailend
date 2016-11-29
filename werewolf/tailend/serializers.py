from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Player


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    """Player Object Serializer"""
    class Meta:
        model = Player
        fields = ('name', 'status')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    """Game Object Serializer"""

    player_list = PlayerSerializer(many=True)
    
    class Meta:
        model = Game
        fields = ('player_list', 'status', 'daynumber', 'stage', 'history')
