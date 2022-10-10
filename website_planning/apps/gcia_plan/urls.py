from django.urls import path, include


urlpatterns = [
    # path("direccion de la web" , "nombre de la funcion en view.py" , "Nombre para acceder a la url desde html")
    path('capex/', include('apps.gcia_plan.capex.dailyCapex.urls')),
    path('capex/', include('apps.gcia_plan.capex.reportesCapex.urls')),
    path('capex/', include('apps.gcia_plan.capex.serviciosCapex.urls')),
    path('materiales/', include('apps.gcia_plan.materiales.dailyMat.urls')),
    path('materiales/', include('apps.gcia_plan.materiales.reportesMat.urls')),
    path('materiales/', include('apps.gcia_plan.materiales.serviciosMat.urls')),
    path('red/', include('apps.gcia_plan.red.dailyRed.urls')),
    path('red/', include('apps.gcia_plan.red.reportesRed.urls')),
    path('red/', include('apps.gcia_plan.red.serviciosRed.urls')),
    ]