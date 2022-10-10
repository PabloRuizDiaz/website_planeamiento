from django.urls import path
from apps.gcia_plan.materiales.serviciosMat.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('servicios/', serviciosMat, name='ServiciosMat'),
    ]