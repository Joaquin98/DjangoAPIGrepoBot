from rest_framework import viewsets
from .serializers import PlayerInfoSerializer
from .models import PlayerInfo


class PlayerInfoViewSet(viewsets.ModelViewSet):
    queryset = PlayerInfo.objects.all().order_by('player_name')
    serializer_class = PlayerInfoSerializer
