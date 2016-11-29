from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Player, History


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'status')


class GameSerializer(serializers.HyperlinkedModelSerializer):

    player_list = PlayerSerializer(many=True)

    class Meta:
        model = Game
        fields = ('player_list', 'status', 'daynumber', 'stage', 'history')
