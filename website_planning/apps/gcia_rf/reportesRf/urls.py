from django.urls import path
from apps.gcia_rf.reportesRf.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('reportes/', reportes, name="ReportesRF"),
    path('reportes/<id_rep>', cargaReporte, name='CargaRepoRF'),
    ]