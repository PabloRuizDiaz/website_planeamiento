from django.urls import path
from apps.apis.views import *
from apps.apis.inicio_web import *
from apps.apis.capex import *
# from apps.apis.vw_spider_pbi import vwSpiderPbi


urlpatterns = [
    path('', apisList, name='APIs'),
    path('sitios_onair/', sitios_onair),
    # path('G5/', G5),
    # path('poblacion_cubierta/', poblacionCubierta),
    path('base_capex/', baseCapex),
    # path('VW_SPIDER_POWERBI/', vwSpiderPbi),
]