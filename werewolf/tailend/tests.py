from django.test import TestCase
from hypothesis import given, settings, HealthCheck
from hypothesis.extra.django.models import models

from tailend.models import *


class TestingEntities(TestCase):
    """A class which tests whether the parameters are being passed correctly"""
    def test_values(self):

        player_owner = Player(name='Nightwing', role='WW')
        player_one = Player(name='Batman', role='VG')
        player_two = Player(name='Joker', role='GH')
        game_one = Game(owner=player_owner, players_list=(player_one,
                                                          player_two),
                        history=History())
        game_one.save()
        game_two = Game(owner=player_owner, players_list=(player_one),
                        history=History())
        game_two.save()

        self.assertEqual(player_owner.name, 'Nightwing')
        self.assertEqual(player_owner.role, 'WW')
        self.assertEqual(player_one.name, 'Batman')
        self.assertEqual(player_one.role, 'VG')
        self.assertEqual(player_two.name, 'Joker')
        self.assertEqual(player_two.role, 'GH')

        # count
        count_player_one = player_one.game_set.count()
        count_player_two = player_two.game_set.count()
        count_owner = player_owner.game_set.count()

        self.assertEqual(count_player_one, 2)
        self.assertEqual(count_player_two, 1)
        self.assertEqual(count_owner, 2)


class TestFieldType(TestCase):
    """A class that generates games and make checks on type of fields"""

    @settings(suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow])
    @given(models(Game, owner=models(Player)), model(Player))

    def test_with_hypothesis(self, game, players):

        game.add(players)

        self.assertTrue(players.game_set.filter(players_slist=players).exists())
