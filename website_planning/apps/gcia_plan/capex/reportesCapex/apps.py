from django.apps import AppConfig


class gciaPlanCapexRepoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.gcia_plan.capex.reportesCapex'
    # label = 'my.label'  # <-- this is the important line - change it to anything other than the default, which is the module name
