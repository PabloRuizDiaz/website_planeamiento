from django.apps import AppConfig


class gciaPlanRedServConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.gcia_plan.red.serviciosRed'
    # label = 'my.label'  # <-- this is the important line - change it to anything other than the default, which is the module name
