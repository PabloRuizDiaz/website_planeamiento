from django.contrib import admin
from apps.gcia_plan.capex.dailyCapex.models import tasasCambioModel


@admin.register(tasasCambioModel)
class TasascambioAdmin(admin.ModelAdmin):
   list_display = ['fecha','pais','tc_plan','tc_revision','tc_proyectada']
   list_filter = ['pais']
   search_fields = ['fecha']
   
   def fecha_mes(self, obj):
        return obj.fecha.strftime("%b-%Y") 