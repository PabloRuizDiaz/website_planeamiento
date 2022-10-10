from django.contrib import admin
# from apps.gcia_plan.red.dailyRed.models import *


# @admin.register(cellIdModel)
# class CellIDsAdmin(admin.ModelAdmin):
#    list_display = ['cell_id','cell_id_old','denominacion','dispo']
#    list_filter = ['dispo']
#    search_fields = ['cell_id','cell_id_old','denominacion']
#    exclude = ['reservado','fecha_reservado']

   
# @admin.register(utModel)
# class UtsAdmin(admin.ModelAdmin):
#    list_display = ['cell_id','ut','tipo_ut','denominacion','activo']
#    list_filter = ['tipo_ut']
#    search_fields = ['cell_id__cell_id','cell_id__cell_id_old','ut','denominacion']
#    actions = ['dar_de_baja', ]

#    def dar_de_baja(self, request, queryset):
#         queryset.update(activo=False)
   
#    dar_de_baja.short_description = "Dar de Baja Seleccionados"