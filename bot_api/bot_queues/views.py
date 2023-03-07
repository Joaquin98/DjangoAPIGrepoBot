from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status


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
    queryset = BuildingOrder.objects.all()
    serializer_class = BuildingOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = super().get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_create(serializer)
        headers = super().get_success_headers(serializer.data)
        return Response({'order_id': serializer.instance.pk}, status=status.HTTP_201_CREATED, headers=headers)


class UnitOrderViewSet(viewsets.ModelViewSet):
    queryset = UnitOrder.objects.all()
    serializer_class = UnitOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = super().get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_create(serializer)
        headers = super().get_success_headers(serializer.data)
        return Response({'order_id': serializer.instance.pk}, status=status.HTTP_201_CREATED, headers=headers)


class ShipOrderViewSet(viewsets.ModelViewSet):
    queryset = ShipOrder.objects.all()
    serializer_class = ShipOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = super().get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_create(serializer)
        headers = super().get_success_headers(serializer.data)
        return Response({'order_id': serializer.instance.pk}, status=status.HTTP_201_CREATED, headers=headers)


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

    def create(self, request, *args, **kwargs):
        serializer = super().get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_create(serializer)

        headers = super().get_success_headers(serializer.data)

        for town_id, settings in request.data['towns'].items():
            settings.update({"town_id": town_id})
            town_serializer = AutocultureTownSettingsSerializer(data=settings)
            town_serializer.is_valid()
            town_serializer.save()
            town_serializer.instance.auto_culture = serializer.instance
            town_serializer.instance.save()

        return Response({'ok': 1}, status=status.HTTP_201_CREATED, headers=headers)


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

    def create(self, request, *args, **kwargs):
        serializer = super().get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().perform_create(serializer)
        headers = super().get_success_headers(serializer.data)
        player = PlayerInfo.objects.get(
            player_id=serializer.instance.player_id,
            world_id=serializer.instance.world_id)
        return Response({'premium_time': player.premium_time}, status=status.HTTP_201_CREATED, headers=headers)
