from django.urls import path
from apps.gcia_ippc.reportesIPPC.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('reportes/', reportes, name="ReportesIPPC"),
    path('reportes/<id_rep>', cargaReporte, name='CargaRepoIPPC'),
    ]