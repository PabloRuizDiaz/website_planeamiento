from django.urls import path
from apps.main.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('', inicio, name="Inicio"),
    path('capex/', gciaPlanCapex, name="Capex"),
    path('materiales/', gciaPlanMateriales, name="Materiales"),
    path('redyproyectos/', gciaPlanRed, name="Red"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('contacto/', contacto, name="Contacto"),
    path('contacto/gracias', gracias, name="Gracias"),
    ]