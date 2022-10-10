from django.contrib import admin
from apps.gcia_plan.red.serviciosRed.models import *

@admin.register(ListPryModelo)
class apisAdmin(admin.ModelAdmin):
    pass

@admin.register(SeguiPryModelo)
class apisAdmin(admin.ModelAdmin):
    pass