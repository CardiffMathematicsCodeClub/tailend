from django.db import models
from ast import literal_eval


class History(object):
    """
    A game history object
    """

    def __init__(self):
        self.history = []

    def from_text(self, txt):
        if len(txt) > 0:
            self.history = literal_eval(txt)
        else:
            self.history = []
        return self

    def to_text(self):
        return str(self.history)

    def add_day(self, lynched, eaten):
        self.history.append((lynched, eaten))


class HistoryField(models.Field):
    description = "A game history for Werewolf"

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def to_python(self, value):
        if isinstance(value, History):
            return value
        return History().from_text(value)

    def get_prep_value(self, value):
        return value.to_text()

    def get_db_prep_value(self, value, connection, prepared=False):
        if prepared:
            return value
        return self.get_prep_value(value)

    def get_internal_type(self):
        return 'TextField'

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class Player(models.Model):
    """Player Class.

    Parameters
    ----------

    -name: Char Field
         player's name
    -id: Char Field
         player's id
    -stage: Char Field
         the stage the player is currently. There are four stages of each
         round of the game
    -role: Char Field
         player's role
    """
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=20, primary_key=True)
    STAGE_CHOICES = (
        ("VG", "Voting"),
        ("VD", "Voted"),
        ("DD", "Dead"),
        ("SG", "Sleeping")
    )
    stage = models.CharField(
        max_length=2,
        choices=STAGE_CHOICES,
        default="SG"
    )
    ROLE_CHOICES = (
        ("VG", "Villager"),
        ("WW", "Werewolf"),
        ("WD", "Witch Doctor"),
        ("GH", "Ghost"),
        ("CT", "Cthulu"),
        ("SR", "Seer")
    )
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=None
    )


class Game(models.Model):
    """Game class.

    Parameters
    ----------

    -owner: Foreign Key
            a player instance that is the game master
    -player_list: ManyToManyField
            a list of player instances
    -status: Char Field
            the status of the game. There can only be three different game status
    -daynumber: Integer Field
            an integer showing in which day the game is currently
    -stage: Char Field
            the stage can either be day or night
    -history: History instance
            the history of the entire game
    """
    owner = models.ForeignKey(Player, related_name="games")
    player_list = models.ManyToManyField(Player)
    STATUS_CHOICES = (
        ("JN", "Joining"),
        ("ST", "Started"),
        ("FN", "Finished")
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default="JN"
    )
    daynumber = models.IntegerField(
        default=0
    )
    STAGE_CHOICES = (
        ("N", "Night"),
        ("D", "Day")
    )
    stage = models.CharField(
        max_length=2,
        choices=STAGE_CHOICES,
        default="N"
    )
    history = HistoryField()
