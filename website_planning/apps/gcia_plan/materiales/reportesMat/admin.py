from django.contrib import admin
from apps.gcia_plan.materiales.reportesMat.models import *


@admin.register(reporteMatModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']