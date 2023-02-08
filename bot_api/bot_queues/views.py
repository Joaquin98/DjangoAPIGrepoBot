from rest_framework import viewsets
from .serializers import *
from .models import *


class PlayerInfoViewSet(viewsets.ModelViewSet):
    queryset = PlayerInfo.objects.all().order_by('player_name')
    serializer_class = PlayerInfoSerializer


class BuildingOrderViewSet(viewsets.ModelViewSet):
    queryset = BuildingOrder.objects.all().order_by('order_id')
    serializer_class = BuildingOrderSerializer
