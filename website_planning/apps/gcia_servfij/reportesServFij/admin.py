from django.contrib import admin
from apps.gcia_servfij.reportesServFij.models import *


@admin.register(reporteServFijModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
