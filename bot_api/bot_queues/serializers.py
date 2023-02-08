from .models import *
from rest_framework import serializers


class AutoBuildSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoBuildSettings
        fields = ('autostart', 'enable_building', 'enable_units',
                  'enable_ships', 'timeinterval', 'instant_buy')


class AutoFarmSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoFarmSettings
        fields = ('autostart', 'method', 'timebetween',
                  'skipwhenfull', 'lowresfirst', 'stoplootbelow')


class AssistantSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssistantSettings
        fields = ('town_names', 'player_name', 'alliance_name', 'auto_relogin')


class BuildingOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildingOrder
        fields = ('order_id', 'player_id', 'player_world',
                  'town_id', 'type', 'item_name', 'count', 'added')


class CityBuildingQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.city_id: BuildingOrderSerializer(BuildingOrder.objects.filter(City=instance.pk), many=True).data}


class CityUnitsQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.city_id: BuildingOrderSerializer(UnitsOrder.objects.filter(City=instance.pk), many=True).data}


class CityShipQueueSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.city_id: BuildingOrderSerializer(ShipOrder.objects.filter(City=instance.pk), many=True).data}


class CityAutocultureSettingsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return super().to_representation(instance)


class AutoCultureCitySettingsSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutoCultureCitySettings
        fields = ('party', 'triumph', 'theater')


class AutocultureCitySettingsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {instance.pk: AutoCultureCitySettingsSerializer2(instance.auto_culture).data}


class AutocultureSettingsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        new_dict = {}
        new_dict['autostart'] = instance.autoculture_settings.autostart
        towns_data = AutocultureCitySettingsSerializer(
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
        fields = ('player_id', 'player_name')


class PlayerInfoSerializer(serializers.HyperlinkedModelSerializer):
    autobuild_settings = AutoBuildSettingsSerializer()
    autofarm_settings = AutoFarmSettingsSerializer()
    assistant_settings = AssistantSettingsSerializer()
    building_queue = CityBuildingQueueSerializer(many=True, read_only=True)
    units_queue = serializers.SerializerMethodField()
    ships_queue = serializers.SerializerMethodField()
    autoculture_settings = serializers.SerializerMethodField()

    class Meta:
        model = PlayerInfo
        fields = ('player_id', 'player_name', 'premium_time',
                  'trial_time', 'facebook_like', 'autobuild_settings',
                  'autofarm_settings', 'assistant_settings', 'building_queue', 'units_queue', 'ships_queue', 'autoculture_settings')

    def get_units_queue(self, obj):
        return CityUnitsQueueSerializer(City.objects.filter(player=obj.pk), many=True).data

    def get_ships_queue(self, obj):
        return CityShipQueueSerializer(City.objects.filter(player=obj.pk), many=True).data

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
