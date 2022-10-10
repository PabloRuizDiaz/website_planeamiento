from django.urls import path
from apps.gcia_plan.capex.serviciosCapex.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('servicios/', serviciosCapex, name='ServiciosCapex'),
    ]