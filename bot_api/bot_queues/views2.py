from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response

class PlayerInfoViewSet(viewsets.ModelViewSet):
    queryset = PlayerInfo.objects.all().order_by('player_name')
    serializer_class = PlayerInfoSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PlayerInfoInputSerializer
        return PlayerInfoSerializer

    def create(self, request, *args, **kwargs):
        players = PlayerInfo.objects.filter(
            player_id=request.data['player_id'], world_id=request.data['world_id'])
        if (len(players) == 0):
            res = super().create(request, *args, **kwargs)
        self.action = 'retrieve'
        self.lookup_url_kwarg = 'pk'
        player = PlayerInfo.objects.filter(
            player_id=request.data['player_id'], world_id=request.data['world_id']).first()
        self.kwargs.update({"pk": player.pk})
        return self.retrieve(request=request)

class BuildingOrderViewSet(viewsets.ModelViewSet):
    queryset = BuildingOrder.objects.all().order_by('order_id')
    serializer_class = BuildingOrderSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UnitOrderViewSet(viewsets.ModelViewSet):
    queryset = UnitOrder.objects.all().order_by('order_id')
    serializer_class = UnitOrderSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UnitOrderInputSerializer
        return UnitOrderSerializer

class ShipOrderViewSet(viewsets.ModelViewSet):
    queryset = ShipOrder.objects.all().order_by('order_id')
    serializer_class = ShipOrderSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ShipOrderInputSerializer
        return ShipOrderSerializer

class AutoBuildSettingsViewSet(viewsets.ModelViewSet):
    queryset = AutoBuildSettings.objects.all()
    serializer_class = AutoBuildSettingsSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return AutoBuildSettingsInputSerializer
        return AutoBuildSettingsSerializer

class AutoFarmSettingsViewSet(viewsets.ModelViewSet):
    queryset = AutoFarmSettings.objects.all()
    serializer_class = AutoFarmSettingsSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return AutoFarmSettingsInputSerializer
        return AutoFarmSettingsSerializer

class AssistantSettingsViewSet(viewsets.ModelViewSet):
    queryset = AssistantSettings.objects.all()
    serializer_class = AssistantSettingsSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return AssistantSettingsInputSerializer
        return AssistantSettingsSerializer

class AutoCultureSettingsViewSet(viewsets.ModelViewSet):
    queryset = AutoCultureSettings.objects.all()
    serializer_class = AutoCultureSettingsSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return AutoCultureSettingsInputSerializer
        return AutoCultureSettingsSerializer

class AutoCultureTownSettingsViewSet(viewsets.ModelViewSet):
    queryset = AutoCultureTownSettings.objects.all()
    serializer_class = AutoCultureTownSettingsSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return AutoCultureTownSettingsInputSerializer
        return AutoCultureTownSettingsSerializer

class PremiumViewSet(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer
