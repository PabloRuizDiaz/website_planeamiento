from django.contrib import admin
from apps.gcia_ippc.reportesIPPC.models import *


@admin.register(reporteIPPCModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
