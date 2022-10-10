from django.contrib import admin
from apps.gcia_tx.reportesTx.models import *


@admin.register(reporteTxModel)
class reportesAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'publicar', 'site', 'tipo', 'visitas']
   search_fields = ['nombre']
