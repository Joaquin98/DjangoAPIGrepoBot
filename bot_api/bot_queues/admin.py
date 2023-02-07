from django.contrib import admin
from .models import *

admin.site.register(BuildingOrder)
admin.site.register(UnitsOrder)
admin.site.register(ShipOrder)
admin.site.register(City)
admin.site.register(AutoBuildSettings)
admin.site.register(AutoFarmSettings)
admin.site.register(AssistantSettings)
admin.site.register(AutoCultureSettings)
admin.site.register(PlayerInfo)