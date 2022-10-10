from django.contrib import admin
from apps.gcia_rf.reportesRf.models import *


@admin.register(reporteRFModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
