from .models import *
from rest_framework import serializers
import time


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


class AutoCultureSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoCultureSettings
        fields = ('autostart',)


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
        fields = ('order_id', 'player_id', 'world_id',
                  'town_id', 'type', 'item_name', 'count', 'added')


class UnitOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildingOrder
        fields = ('order_id', 'player_id', 'world_id',
                  'town_id', 'type', 'item_name', 'count', 'added')


class ShipOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildingOrder
        fields = ('order_id', 'player_id', 'world_id',
                  'town_id', 'type', 'item_name', 'count', 'added')


class TownBuildingQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: BuildingOrderSerializer(BuildingOrder.objects.filter(Towns=instance.pk), many=True).data}

class BuildingOrderAllSerializer(serializers.Serializer):

    def to_representation(self, instance):
        data = {}
        item_data = super().to_representation(instance)
        print(instance.pk)
        player = PlayerInfo.objects.filter(player_id=instance.player_id, world_id=instance.world_id).first()
        res = TownBuildingQueueSerializer(Town.objects.filter(player=player.pk), many=True).data
        
        for element in res:
            for key, val in element.items():
                data.update({key: val})
        
        data.update({'item': BuildingOrderSerializer(BuildingOrder.objects.get(pk = instance.pk)).data})

        return data

    class Meta:
        model = BuildingOrder
        fields = ('order_id', 'player_id', 'world_id',
                'town_id', 'type', 'item_name', 'count', 'added')
    

class TownUnitsQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: UnitOrderSerializer(UnitOrder.objects.filter(Towns=instance.pk), many=True).data}


class TownShipQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: ShipOrderSerializer(ShipOrder.objects.filter(Towns=instance.pk), many=True).data}


class TownAutocultureSettingsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return super().to_representation(instance)


class AutoCultureTownSettingsSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoCultureTownSettings
        fields = ('party', 'triumph', 'theater')


class AutocultureTownSettingsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.town_id: AutoCultureTownSettingsSerializer2(instance.auto_culture).data}


class AutocultureSettingsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        new_dict = {}
        new_dict['autostart'] = instance.autoculture_settings.autostart
        towns_data = AutocultureTownSettingsSerializer(
            instance.building_queue, many=True).data
        new_towns_data = {}
        for element in towns_data:
            for key, value in element.items():
                new_towns_data.update({key: value})
        new_dict['towns'] = new_towns_data

        return new_dict


class PlayerInfoInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = ('locale_lang', 'player_id', 'player_name',
                  'world_id', 'premium_grepolis')


class PlayerInfoSerializer(serializers.HyperlinkedModelSerializer):
    autobuild_settings = AutoBuildSettingsSerializer()
    autofarm_settings = AutoFarmSettingsSerializer()
    assistant_settings = AssistantSettingsSerializer()
    building_queue = TownBuildingQueueSerializer(many=True, read_only=True)
    units_queue = serializers.SerializerMethodField()
    ships_queue = serializers.SerializerMethodField()
    autoculture_settings = serializers.SerializerMethodField()

    class Meta:
        model = PlayerInfo
        fields = ('player_id', 'player_name', 'premium_time',
                  'trial_time', 'facebook_like', 'autobuild_settings',
                  'autofarm_settings', 'assistant_settings', 'building_queue', 'units_queue', 'ships_queue', 'autoculture_settings')

    def get_units_queue(self, obj):
        return TownUnitsQueueSerializer(Town.objects.filter(player=obj.pk), many=True).data

    def get_ships_queue(self, obj):
        return TownShipQueueSerializer(Town.objects.filter(player=obj.pk), many=True).data

    def get_autoculture_settings(self, obj):
        if obj.autoculture_settings:
            return AutocultureSettingsSerializer(obj).data
        return {}

    def to_representation(self, instance):
        data = super(PlayerInfoSerializer, self).to_representation(instance)

        building_queue = data.pop('building_queue')
        new_dict = {}
        for element in building_queue:
            for key, val in element.items():
                new_dict.update({key: val})
        data.update({'building_queue': new_dict})

        units_queue = data.pop('units_queue')
        new_dict = {}
        for element in units_queue:
            for key, val in element.items():
                new_dict.update({key: val})
        data.update({'units_queue': new_dict})

        ships_queue = data.pop('ships_queue')
        new_dict = {}
        for element in ships_queue:
            for key, val in element.items():
                new_dict.update({key: val})
        data.update({'ships_queue': new_dict})

        return data


class BuildingOrderInputSerializer(serializers.HyperlinkedModelSerializer):
    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        try:
            town = player.building_queue.get(
                town_id=self._validated_data['town_id'])
        except Exception:
            town = Town(
                town_id=self._validated_data['town_id'], player=player, auto_culture=None)
            town.save()

        try:
            order_id = town.cities.all().order_by('order_id').last().order_id + 1
        except Exception:
            order_id = 1

        self._validated_data.update({
            'Towns': town})
        self._validated_data.update({'order_id': order_id})
        return super().save(**kwargs)

    class Meta:
        model = BuildingOrder
        fields = ('player_id', 'world_id', 'town_id', 'item_name')


class UnitOrderInputSerializer(serializers.HyperlinkedModelSerializer):
    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        try:
            town = player.building_queue.get(
                town_id=self._validated_data['town_id'])
        except Exception:
            town = Town(
                town_id=self._validated_data['town_id'], player=player, auto_culture=None)
            town.save()

        try:
            order_id = town.cities.all().order_by('order_id').last().order_id + 1
        except Exception:
            order_id = 1

        self._validated_data.update({
            'Towns': town})
        self._validated_data.update({'order_id': order_id})
        return super().save(**kwargs)

    class Meta:
        model = UnitOrder
        fields = ('player_id', 'world_id', 'town_id', 'item_name')


class ShipOrderInputSerializer(serializers.HyperlinkedModelSerializer):
    def save(self, **kwargs):

        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        try:
            town = player.building_queue.get(
                town_id=self._validated_data['town_id'])
        except Exception:
            town = Town(
                town_id=self._validated_data['town_id'], player=player, auto_culture=None)
            town.save()

        try:
            order_id = town.cities.all().order_by('order_id').last().order_id + 1
        except Exception:
            order_id = 1

        self._validated_data.update({
            'Towns': town})
        self._validated_data.update({'order_id': order_id})
        return super().save(**kwargs)

    class Meta:
        model = ShipOrder
        fields = ('player_id', 'world_id', 'town_id', 'item_name')


class PremiumSerializer(serializers.HyperlinkedModelSerializer):

    def save(self, **kwargs):
        player = PlayerInfo.objects.get(
            player_id=self._validated_data['player_id'],
            world_id=self._validated_data['world_id'])

        days_map = {
            3.99: 30*86400,
            8.99: 72*86400,
            18.99: 156*86400,
            48.99: 420*86400
        }

        player.premium_time = player.premium_time + \
            days_map[self._validated_data['price']]

        player.save()

        return super().save(**kwargs)

    class Meta:
        model = Premium
        fields = ('player_id', 'world_id', 'price', 'date')
