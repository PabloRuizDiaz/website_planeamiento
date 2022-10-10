from django.contrib import admin
from apps.gcia_plan.capex.reportesCapex.models import *


@admin.register(reporteCapexModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
