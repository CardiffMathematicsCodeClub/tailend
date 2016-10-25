from django.db import models

# Create your models here.

class Game(models.Model):
    """
    Manage game state
    """
    owner = models.ForeignKey("Player", related_name="games")
    STATUS_CHOICES = (
            ("JN", "Joining"),
            ("ST", "Started"),
            ("FN", "Finished")
            )
    status = models.CharField(
            max_length = 2,
            choices = STATUS_CHOICES,
            default = "JN"
            )
    daynumber = models.IntegerField()
    STAGE_CHOICES = (
            ("N", "Night"),
            ("D", "Day")
            )
    stage = models.CharField(
            max_length = 2,
            choices = STAGE_CHOICES,
            default = "N"
            )
    history = HistoryField()


class Player(models.Model):
    """
    Manage player state
    """
    name = models.CharField()
    STATUS_CHOICES = (
            ("VG", "Voting"),
            ("VD", "Voted"),
            ("DD", "Dead"),
            ("SG", "Sleeping")
            )
    status = models.CharField(
            max_length = 2,
            choices = STATUS_CHOICES,
            default = "SG"
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
            max_length = 2,
            choices = ROLE_CHOICES,
            default = None
            )
