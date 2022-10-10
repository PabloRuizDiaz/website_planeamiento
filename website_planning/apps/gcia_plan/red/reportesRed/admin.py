from django.contrib import admin
from apps.gcia_plan.red.reportesRed.models import *


@admin.register(reporteRedModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
