from django.db import models


class tasasCambioModel(models.Model):
    fecha = models.DateField()
    pais = models.CharField(max_length=10)
    tc_plan = models.FloatField(blank=True, null=True)
    tc_revision = models.FloatField(blank=True, null=True)
    tc_proyectada = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'WEB_DAILYTASASCAMBIO'
        ordering = ["fecha","pais"]


class pospreModel(models.Model):
    POSPRE = models.CharField(max_length=12,verbose_name='POSPRE')
    DESCRIPCION_POSPRE = models.CharField(max_length=75,verbose_name='DESCRIPCION_POSPRE')
    RUBRO = models.CharField(max_length=100,verbose_name='RUBRO')
    RUBRO_1 = models.CharField(max_length=100,verbose_name='RUBRO_1')
    RED = models.CharField(max_length=2,verbose_name='RED')

    class Meta:
        db_table = 'WEB_DAILYPOSPRE'


class pospreFileModel(models.Model):
    DOC_POSPRE = models.FileField(upload_to='gcia_plan/capex/files')

    class Meta:
        db_table = 'WEB_FILEPOSPRE'


class proveedorModel(models.Model):
    NROPROVEEDOR = models.IntegerField(verbose_name='NROPROVEEDOR')
    PROVEEDOR = models.CharField(max_length=50,verbose_name='PROVEEDOR')
    COMEX = models.IntegerField(verbose_name='COMEX')

    class Meta:
        db_table = 'WEB_DAILYPROVEEDORES'


class pryCarryOverModel(models.Model):
    POSPRE=models.CharField(max_length=12,verbose_name='POSPRE')
    CEGE = models.CharField(max_length=10,verbose_name='CEGE')
    DENOM_CEGE = models.CharField(max_length=100,verbose_name='DENOM_CEGE')
    PRESUPUESTO_ANIO = models.IntegerField()
    FONDO = models.CharField(max_length=10,verbose_name='FONDO')
    CAPEX_FINAL = models.FloatField()
    
    class Meta:
        db_table = 'WEB_DAILYCARRYOVER'


class pryCarryOverFileModel(models.Model):
    DOC_PRY_CO = models.FileField(upload_to='gcia_plan/capex/files')

    class Meta:
        db_table = 'WEB_FILECARRYOVER'