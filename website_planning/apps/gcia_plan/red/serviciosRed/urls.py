from django.urls import path  
from apps.gcia_plan.red.serviciosRed.views import *

urlpatterns = [
    path('servicios/', serviciosRed, name='ServiciosRed'),
    path('servicios/proyectosCore', main_proyecto_core, name='PryCore'),
    path('servicios/nuevo_proyecto/', nuevo_proyecto_core, name='PryCoreNuevo'),
    path('servicios/actualizar_proyecto/', actualizar_proyecto_core, name='PryCoreActualizar'),
    path('servicios/actualizar_estado/', actualizar_estado_proyecto_core, name='PryCoreEstado'),
    # path('servicios/SMC/', listadoSitios, name='SMC'),
    # path('servicios/SMC/masivo/', listadoMasivoSitios, name='SMCMasivo'),
    # path('servicios/UTviewer/', viewUT, name='UTViewer'),
    # path('servicios/sitios_localidad/', viewSitiosLocal, name='SitiosLocal'),
    # path('servicios/base_historica_celdas/', viewHistoricoCeldas, name='HistoricoCeldas'),
    # path('servicios/sitios_calles/', viewSitiosCalles, name='CalleSitios'),
]