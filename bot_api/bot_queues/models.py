from django.db import models
from datetime import datetime


class AutoBuildSettings(models.Model):
    autostart = models.BooleanField()
    enable_building = models.BooleanField()
    enable_units = models.BooleanField()
    enable_ships = models.BooleanField()
    timeinterval = models.IntegerField()
    instant_buy = models.BooleanField()
    player_id = models.IntegerField()
    world_id = models.CharField(max_length=30)


class AutoFarmSettings(models.Model):
    autostart = models.BooleanField()
    method = models.IntegerField()
    timebetween = models.IntegerField()
    skipwhenfull = models.BooleanField()
    lowresfirst = models.BooleanField()
    stoplootbelow = models.BooleanField()
    player_id = models.IntegerField(default=None)
    world_id = models.CharField(max_length=30, default=None)


class AssistantSettings(models.Model):
    town_names = models.BooleanField()
    player_name = models.BooleanField()
    alliance_name = models.BooleanField()
    auto_relogin = models.IntegerField()
    player_id = models.IntegerField(default=None)
    world_id = models.CharField(max_length=30, default=None)


class AutoCultureSettings(models.Model):
    autostart = models.BooleanField()
    player_id = models.IntegerField(default=None)
    world_id = models.CharField(max_length=30, default=None)


class AutoCultureTownSettings(models.Model):
    party = models.BooleanField()
    triumph = models.BooleanField()
    theater = models.BooleanField()
    player_id = models.IntegerField(default=None)
    town_id = models.IntegerField(default=None)
    world_id = models.CharField(max_length=30, default=None)


class PlayerInfo(models.Model):
    locale_lang = models.CharField(
        max_length=50, blank=True, null=True, default="")
    player_id = models.IntegerField()
    player_name = models.CharField(max_length=100)
    world_id = models.CharField(
        max_length=50, blank=True, null=True, default="")
    premium_grepolis = models.BooleanField(default=False)
    premium_time = models.IntegerField(blank=True, null=True)
    trial_time = models.IntegerField(blank=True, null=True)
    facebook_like = models.IntegerField(blank=True, null=True)
    autobuild_settings = models.OneToOneField(
        AutoBuildSettings, on_delete=models.CASCADE, blank=True, null=True)
    autofarm_settings = models.OneToOneField(
        AutoFarmSettings, on_delete=models.CASCADE, blank=True, null=True)
    autoculture_settings = models.OneToOneField(
        AutoCultureSettings, on_delete=models.CASCADE, blank=True, null=True, related_name='autoculture_settings')
    assistant_settings = models.OneToOneField(
        AssistantSettings, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return ("Jugador %s" % self.player_name)


class Town(models.Model):
    town_id = models.IntegerField()
    player = models.ForeignKey(
        PlayerInfo, related_name='building_queue', on_delete=models.CASCADE, blank=True, null=True)
    auto_culture = models.OneToOneField(
        AutoCultureTownSettings, on_delete=models.CASCADE, blank=True, null=True)


class BuildingOrder(models.Model):
    Towns = models.ForeignKey(
        Town, on_delete=models.CASCADE, related_name='cities', default=None, null=True)
    order_id = models.IntegerField(default=1)
    player_id = models.IntegerField()
    player_world = models.CharField(max_length=20)
    town_id = models.IntegerField()
    type = models.CharField(max_length=20, default="building")
    item_name = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    added = models.DateTimeField(
        default=datetime.now())

    def __str__(self) -> str:
        return ("Item: %s, Town Id : %s" % (self.item_name, self.town_id))


class UnitsOrder(models.Model):
    Towns = models.ForeignKey(Town, on_delete=models.CASCADE, default=None)


class ShipOrder(models.Model):
    Towns = models.ForeignKey(Town, on_delete=models.CASCADE, default=None)
