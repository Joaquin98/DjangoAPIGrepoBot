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

    def get_serializer_class(self):
        if self.action == 'create':
            return BuildingOrderInputSerializer
        return BuildingOrderSerializer
