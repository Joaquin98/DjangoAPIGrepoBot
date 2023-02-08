from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response


class PlayerInfoViewSet(viewsets.ModelViewSet):
    queryset = PlayerInfo.objects.all().order_by('player_name')
    serializer_class = PlayerInfoSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PlayerInfoSerializer
        if self.action == 'create':
            return PlayerInfoInputSerializer
        return PlayerInfoSerializer

    def create(self, request, *args, **kwargs):
        if (len(PlayerInfo.objects.filter(pk=request.data['player_id'])) > 0):
            self.action = 'list'
            return self.list(request=request, pk=request.data['player_id'])
        else:
            return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if ('pk' in kwargs.keys()):
            self.queryset = PlayerInfo.objects.filter(
                pk=kwargs['pk'])

        return super().list(request, *args, **kwargs)


class BuildingOrderViewSet(viewsets.ModelViewSet):
    queryset = BuildingOrder.objects.all().order_by('order_id')
    serializer_class = BuildingOrderSerializer
