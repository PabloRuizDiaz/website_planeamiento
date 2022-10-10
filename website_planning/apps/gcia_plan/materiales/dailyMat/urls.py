from django.urls import path
from apps.gcia_plan.materiales.dailyMat.views import *

urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('daily/', dailyMat, name='DailyMat'),
    ]