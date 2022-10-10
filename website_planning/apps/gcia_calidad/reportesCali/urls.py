from django.urls import path
from apps.gcia_calidad.reportesCali.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('reportes/', reportes, name="ReportesCalidad"),
    path('reportes/<id_rep>', cargaReporte, name='CargaRepoCali'),
    ]