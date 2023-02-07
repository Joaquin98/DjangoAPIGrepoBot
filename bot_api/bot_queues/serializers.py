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


class TrackListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {value.city_id: []}


class CitySerializer(serializers.HyperlinkedModelSerializer):
    # BuildingOrderSerializer(many=True)
    aaa = TrackListingField(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('aaa', 'party', 'triumph', 'theater')


class CitySeri(serializers.RelatedField):

    def to_representation(self, value):
        return {value.city_id: [BuildingOrder.objects.all()]}


class PlayerInfoSerializer(serializers.HyperlinkedModelSerializer):
    autobuild_settings = AutoBuildSettingsSerializer()
    autofarm_settings = AutoFarmSettingsSerializer()
    assistant_settings = AssistantSettingsSerializer()
    building_queue = CitySeri(many=True, read_only=True)

    def in_name(self, foo):
        return CitySerializer()

    class Meta:
        model = PlayerInfo
        fields = ('player_name', 'premium_time',
                  'trial_time', 'facebook_like', 'autobuild_settings',
                  'autofarm_settings', 'assistant_settings', 'building_queue')
