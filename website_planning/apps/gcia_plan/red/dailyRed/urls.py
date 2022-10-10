from django.urls import path 
from apps.gcia_plan.red.dailyRed.views import *


urlpatterns = [
    path('daily/', daily, name='DailyRed'),
    # path('daily/altaUbicacionTecnica/', altaUT, name='AltaUT'),
    # path('daily/altaUTMasiva/', altaMasivaUT, name='AltaMasivaUT'),
]