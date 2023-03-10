from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerInfoViewSet)
router.register(r'buildingorder', views.BuildingOrderViewSet)
router.register(r'unitorder', views.UnitOrderViewSet)
router.register(r'shiporder', views.ShipOrderViewSet)
router.register(r'buildsettings', views.AutoBuildSettingsViewSet)
router.register(r'farmsettings', views.AutoFarmSettingsViewSet)
router.register(r'assistantsettings', views.AssistantSettingsViewSet)
router.register(r'culturesettings', views.AutoCultureSettingsViewSet)
router.register(r'culturetownsettings', views.AutoCultureTownSettingsViewSet)
router.register(r'premium', views.PremiumViewSet)
router.register(r'support', views.SupportViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
