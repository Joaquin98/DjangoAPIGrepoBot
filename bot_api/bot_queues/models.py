from django.db import models


class AutoBuildSettings(models.Model):
    autostart = models.BooleanField()
    enable_building = models.BooleanField()
    enable_units = models.BooleanField()
    enable_ships = models.BooleanField()
    timeinterval = models.IntegerField()
    instant_buy = models.BooleanField()


class AutoFarmSettings(models.Model):
    autostart = models.BooleanField()
    method = models.IntegerField()
    timebetween = models.IntegerField()
    skipwhenfull = models.BooleanField()
    lowresfirst = models.BooleanField()
    stoplootbelow = models.BooleanField()


class AssistantSettings(models.Model):
    town_names = models.BooleanField()
    player_name = models.BooleanField()
    alliance_name = models.BooleanField()
    auto_relogin = models.IntegerField()


class AutoCultureSettings(models.Model):
    autostart = models.BooleanField()


class AutoCultureCitySettings(models.Model):
    party = models.BooleanField()
    triumph = models.BooleanField()
    theater = models.BooleanField()


class PlayerInfo(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100)
    premium_time = models.IntegerField()
    trial_time = models.IntegerField()
    facebook_like = models.IntegerField()
    autobuild_settings = models.OneToOneField(
        AutoBuildSettings, on_delete=models.CASCADE, blank=True, null=True)
    autofarm_settings = models.OneToOneField(
        AutoFarmSettings, on_delete=models.CASCADE, blank=True, null=True)
    autoculture_settings = models.OneToOneField(
        AutoCultureSettings, on_delete=models.CASCADE, blank=True, null=True)
    assistant_settings = models.OneToOneField(
        AssistantSettings, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return ("Jugador %s" % self.player_name)


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(
        PlayerInfo, related_name='building_queue', on_delete=models.CASCADE, blank=True, null=True)
    auto_culture = models.OneToOneField(
        AutoCultureCitySettings, on_delete=models.CASCADE, blank=True, null=True)


class BuildingOrder(models.Model):
    City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='aaa', default=None)
    order_id = models.IntegerField()
    player_id = models.IntegerField()
    player_world = models.CharField(max_length=20)
    town_id = models.IntegerField()
    type = models.CharField(max_length=20)
    item_name = models.CharField(max_length=100)
    count = models.IntegerField()
    added = models.DateTimeField()

    def __str__(self) -> str:
        return ("Item: %s, Town Id : %s" % (self.item_name, self.town_id))


class UnitsOrder(models.Model):
    City = models.ForeignKey(City, on_delete=models.CASCADE, default=None)
    pass


class ShipOrder(models.Model):
    City = models.ForeignKey(City, on_delete=models.CASCADE, default=None)
    pass
