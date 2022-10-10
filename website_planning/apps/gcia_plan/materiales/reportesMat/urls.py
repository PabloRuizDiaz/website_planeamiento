from django.urls import path
from apps.gcia_plan.materiales.reportesMat.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('reportes/', reportesMat, name='ReportesMat'),
    path('reportes/<id_rep>', cargaReporte, name='CargaRepoMat'),
    ]