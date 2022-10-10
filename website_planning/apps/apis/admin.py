from django.contrib import admin
from apps.apis.models import *


@admin.register(ListApiModelo)
class apisAdmin(admin.ModelAdmin):
    list_filter = ('PUBLICACION',)
    list_display = ('ID','NOMBRE','PUBLICACION')
    search_fields = ['ID','NOMBRE']