from .models import *
from rest_framework import serializers
import time
from datetime import datetime


class AutoBuildSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoBuildSettings
        fields = ('autostart', 'enable_building', 'enable_units',
                  'enable_ships', 'timeinterval', 'instant_buy')


class AutoBuildSettingsInputSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AutoBuildSettings
        fields = ('autostart', 'enable_building', 'enable_units',
                  'enable_ships', 'timeinterval', 'instant_buy', 'player_id', 'world_id')

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'], world_id=self._validated_data['world_id'])

        build_settings_object = super().save(**kwargs)

        player.autobuild_settings = build_settings_object

        player.save()

        return build_settings_object


class AutoFarmSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoFarmSettings
        fields = ('autostart', 'method', 'timebetween',
                  'skipwhenfull', 'lowresfirst', 'stoplootbelow')


class AutoFarmSettingsInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoFarmSettings
        fields = ('autostart', 'method', 'timebetween',
                  'skipwhenfull', 'lowresfirst', 'stoplootbelow', 'player_id', 'world_id')

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'], world_id=self._validated_data['world_id'])

        farm_settings_object = super().save(**kwargs)

        player.autofarm_settings = farm_settings_object

        player.save()

        return farm_settings_object


class AssistantSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssistantSettings
        fields = ('town_names', 'player_name', 'alliance_name', 'auto_relogin')


class AssistantSettingsInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssistantSettings
        fields = ('town_names', 'player_name', 'alliance_name',
                  'auto_relogin', 'player_id', 'world_id')

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'], world_id=self._validated_data['world_id'])

        assistant_settings_object = super().save(**kwargs)

        player.assistant_settings = assistant_settings_object

        player.save()

        return assistant_settings_object


class AutoCultureSettingsInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoCultureSettings
        fields = ('autostart', 'player_id', 'world_id')

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'], world_id=self._validated_data['world_id'])

        autoculture_settings_object = super().save(**kwargs)

        player.autoculture_settings = autoculture_settings_object

        player.save()

        return autoculture_settings_object


class AutoCultureTownSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoCultureTownSettings
        fields = ('party', 'triumph', 'theater')


class AutoCultureTownSettingsInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoCultureTownSettings
        fields = ('party', 'triumph', 'theater',
                  'town_id', 'player_id', 'world_id')

    def save(self, **kwargs):

        town = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'], world_id=self._validated_data['world_id']).building_queue.get(town_id=self._validated_data['town_id'])

        autoculturetown_settings_object = super().save(**kwargs)

        town.auto_culture = autoculturetown_settings_object

        town.save()

        return autoculturetown_settings_object


class BuildingOrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BuildingOrder
        fields = ('player_id', 'world_id', 'town_id', 'item_name', 'added')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({'id': instance.pk})
        return data

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        try:
            town = player.towns.get(town_id=self._validated_data['town_id'])
        except Exception:
            town = Town(
                town_id=self._validated_data['town_id'], player=player, auto_culture=None)
            town.save()

        self._validated_data.update({
            'town_obj': town})

        return super().save(**kwargs)


class UnitOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitOrder
        fields = ('player_id', 'world_id',
                  'town_id', 'item_name', 'count', 'added')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({'id': instance.pk})
        return data

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        try:
            town = player.towns.get(town_id=self._validated_data['town_id'])
        except Exception:
            town = Town(
                town_id=self._validated_data['town_id'], player=player, auto_culture=None)
            town.save()

        self._validated_data.update({
            'town_obj': town})

        return super().save(**kwargs)


class ShipOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShipOrder
        fields = ('player_id', 'world_id',
                  'town_id', 'item_name', 'count', 'added')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({'id': instance.pk})
        return data

    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        try:
            town = player.towns.get(town_id=self._validated_data['town_id'])
        except Exception:
            town = Town(
                town_id=self._validated_data['town_id'], player=player, auto_culture=None)
            town.save()

        self._validated_data.update({
            'town_obj': town})

        return super().save(**kwargs)


class TownBuildingQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: BuildingOrderSerializer(BuildingOrder.objects.filter(town_obj=instance.pk), many=True).data}


class TownUnitsQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: UnitOrderSerializer(UnitOrder.objects.filter(town_obj=instance.pk), many=True).data}


class TownShipQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: ShipOrderSerializer(ShipOrder.objects.filter(town_obj=instance.pk), many=True).data}


class AutocultureTownSettingsSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('town_id')
        return data

    class Meta:
        model = AutoCultureTownSettings
        fields = ('party', 'triumph', 'theater', 'town_id')


class AutocultureTownIdSettingsSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {instance.town_id: AutoCultureTownSettingsSerializer(instance).data}


class AutoCultureSettingsSerializer(serializers.HyperlinkedModelSerializer):
    town_settings = AutocultureTownIdSettingsSerializer(
        many=True, read_only=True)

    def save(self, **kwargs):

        res = super().save(**kwargs)

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'], world_id=self._validated_data['world_id'])

        if player.autoculture_settings != None:
            player.autoculture_settings.delete()

        player.autoculture_settings = res
        player.save()

        return res

    def to_representation(self, instance):
        data = super().to_representation(instance)
        towns_data = data.pop('town_settings')
        data.pop('player_id')
        data.pop('world_id')
        new_dict = {}
        for town_data in towns_data:
            for key, value in town_data.items():
                new_dict.update({key: value})
        data.update({'towns': new_dict})
        return data

    class Meta:
        model = AutoCultureSettings
        fields = ('autostart', 'player_id', 'world_id', 'town_settings')


class PlayerInfoInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = ('locale_lang', 'player_id', 'player_name',
                  'world_id', 'premium_grepolis')


class PlayerInfoSerializer(serializers.HyperlinkedModelSerializer):
    autobuild_settings = AutoBuildSettingsSerializer()
    autofarm_settings = AutoFarmSettingsSerializer()
    assistant_settings = AssistantSettingsSerializer()
    building_queue = serializers.SerializerMethodField()
    units_queue = serializers.SerializerMethodField()
    ships_queue = serializers.SerializerMethodField()
    autoculture_settings = serializers.SerializerMethodField()

    class Meta:
        model = PlayerInfo
        fields = ('player_id', 'player_name', 'premium_time',
                  'trial_time', 'facebook_like', 'autobuild_settings',
                  'autofarm_settings', 'assistant_settings', 'building_queue', 'units_queue', 'ships_queue', 'autoculture_settings')

    def get_units_queue(self, obj):
        return TownUnitsQueueSerializer(obj.towns.all(), many=True).data

    def get_ships_queue(self, obj):
        return TownShipQueueSerializer(obj.towns.all(), many=True).data

    def get_building_queue(self, obj):
        return TownBuildingQueueSerializer(obj.towns.all(), many=True, read_only=True).data

    def get_autoculture_settings(self, obj):
        if obj.autoculture_settings:
            return AutoCultureSettingsSerializer(obj.autoculture_settings).data
        return {}

    def to_representation(self, instance):
        data = super(PlayerInfoSerializer, self).to_representation(instance)

        building_queue = data.pop('building_queue')
        new_dict = {}
        for element in building_queue:
            for key, val in element.items():
                if len(val):
                    new_dict.update({key: val})
        data.update({'building_queue': new_dict})

        units_queue = data.pop('units_queue')
        new_dict = {}
        for element in units_queue:
            for key, val in element.items():
                if len(val):
                    new_dict.update({key: val})
        data.update({'units_queue': new_dict})

        ships_queue = data.pop('ships_queue')
        new_dict = {}
        for element in ships_queue:
            for key, val in element.items():
                if len(val):
                    new_dict.update({key: val})
        data.update({'ships_queue': new_dict})

        return data


class PremiumSerializer(serializers.HyperlinkedModelSerializer):

    def save(self, **kwargs):
        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        days_map = {
            4.99: 30*86400,
            9.99: 72*86400,
            19.99: 156*86400,
            49.99: 420*86400
        }

        player.premium_time = max([time.mktime(datetime.now().timetuple()), player.premium_time]) + \
            days_map[self._validated_data['price']]

        player.save()

        return super().save(**kwargs)

    class Meta:
        model = Premium
        fields = ('player_id', 'world_id', 'price')


class SupportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"
