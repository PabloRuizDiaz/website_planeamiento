from django.contrib import admin
from apps.gcia_calidad.reportesCali.models import *


@admin.register(reporteCalidadModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
