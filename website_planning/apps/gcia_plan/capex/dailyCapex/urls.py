from django.urls import path
from apps.gcia_plan.capex.dailyCapex.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde Django")
    path('daily/', daily, name='DailyCapex'),
    path('daily/tasaCambio/', tasaCambio, name='TasaCambio'),
    path('daily/cargaPospre/', pospre, name='CargaPosPre'),
    path('daily/proveedores/', proveedores, name='Proveedores'),
    path('daily/carry_over/', carryOver, name='CarryOver'),
]