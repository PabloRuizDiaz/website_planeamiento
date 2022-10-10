from django.db import models
from django.utils.translation import gettext_lazy as _


class reporteIPPCModel(models.Model):
    class tipo_Reporte(models.TextChoices):
        Tableau = 'TAB', _('Tableau')
        PowerBi = 'PBI', _('Power BI')

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(
        max_length=3,
        choices=tipo_Reporte.choices,
        default=tipo_Reporte.Tableau)
    url_pwbi = models.CharField(
        max_length=500,
        null=True,
        blank=True)
    site = models.CharField(
        max_length=30,
        default='PlaneacindeRed', 
        null=True,
        blank=True)
    user_auth = models.CharField(
        max_length=8,
        null=True,
        blank=True)
    view_id = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    descripcion = models.TextField()
    visitas = models.IntegerField(
        default=0)
    publicar = models.BooleanField(
        default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'WEB_REPORTEIPPC'