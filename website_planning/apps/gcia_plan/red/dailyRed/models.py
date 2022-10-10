# from django.db import models
# from django.utils.translation import gettext_lazy as _


# class cellIdModel(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cell_id = models.CharField(max_length=10,unique=True)
#     cell_id_old = models.CharField(max_length=10,unique=True)
#     denominacion = models.CharField(max_length=100, blank=True, null=True)
#     latitud = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
#     longitud = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
#     direccion = models.CharField(max_length=200, blank=True, null=True)
#     localidad = models.CharField(max_length=100, blank=True, null=True)
#     departamento = models.CharField(max_length=50, blank=True, null=True)
#     provincia = models.CharField(max_length=55, blank=True, null=True)
#     pais = models.CharField(max_length=30, blank=True, null=True)
#     alm = models.CharField(max_length=5, blank=True, null=True)
#     reservado = models.BooleanField(default=False)
#     fecha_reservado = models.DateTimeField(null=True)
#     dispo = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if cellIdModel.objects.filter(cell_id=self.cell_id).exists():
#             cell = cellIdModel.objects.get(cell_id=self.cell_id)
            
#             if cell.uts.count() > 0:
#                 self.dispo = False

#         return super().save(*args, **kwargs)

#     def __str__(self):
#         return self.cell_id
    
#     class Meta:
#         db_table = 'Cell_id_Django'
#         ordering = ["cell_id"]


# class utModel(models.Model):
#     class Tipo_ut(models.TextChoices):
#         INFRA_MOV = 'IM', _('INFRAESTRUCTURA MOVIL')
#         INFRA_FIJA = 'IF', _('INFRAESTRUCTURA FIJA')
#         LOCA_COM = 'LC', _('LOCALES COMERCIALES')
#         CANONES = 'CN',	_('CANONES')
#         CAC = 'CV',	_('CAC')
#         CORPO_MOVIL = 'CPM', _('MOVIL CORPORATIVAS')
#         DATA_CENTER_MOV = 'DCM', _('MOVIL DATA CENTERS')
#         ACCES_EMP = 'EM', _('ACCESOS EMPRESARIALES')
#         CORPO_FIJA = 'CPF', _('FIJA CORPORATIVAS')
#         DATA_CENTER_FIJA = 'DCF', _('FIJA DATA CENTERS')
#         WAREHOUSE = 'BD', _('WAREHOUSE')
#         TORRERA = 'TR', _('TORRERA')
    
#     id = models.BigAutoField(primary_key=True)
#     tipo_ut = models.CharField(max_length=3,choices=Tipo_ut.choices,default=Tipo_ut.INFRA_MOV)
#     ut = models.CharField(max_length=30)
#     denominacion = models.CharField(max_length=255)
#     cell_id = models.ForeignKey(cellIdModel, on_delete=models.PROTECT,null=False,blank=False,related_name='uts')
#     creador = models.CharField(max_length=20, null=True, blank=True)
#     activo = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         c = self.ut.split('-')[-1]
#         c = c[:7].upper()
#         cell = cellIdModel.objects.filter(cell_id=c).first()
#         cell.dispo = False
#         cell.save()

#         return super(utModel, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.ut

#     class Meta:
#         db_table = 'UT_Django'
#         ordering = ["ut"]


# class Sap_BI:
#     def __init__(self, ut, tipo, estructura, denominacion, grupo, centro_empl, empl, ceco, sociedad, LOCALIDAD, Departamento,provincia,latitud,longitud,alm):
#         nombre_pais={'AR':'ARGENTINA','UY':'URUGUAY','PY':'PARAGUAY'}
#         self.ut=ut
#         self.tipo_ut=ut.split('-')[4]
#         self.tipo=tipo
#         self.estructura=estructura
#         self.denominacion=denominacion
#         self.grupo=grupo
#         self.centro_empl=centro_empl
#         self.empl=empl
#         self.ceco=ceco
#         self.sociedad=sociedad
#         self.cell_id=ut.split('-')[5]
#         self.localidad= LOCALIDAD
#         self.departamento=Departamento
#         self.provincia=provincia
#         self.pais=nombre_pais[ut.split('-')[0]]
#         self.lat=latitud
#         self.long=longitud
#         self.alm=alm


# class utFileModel(models.Model):
#     DOC_UT = models.FileField(upload_to='gcia_plan/red/files')

#     class Meta:
#         db_table = 'WEB_FILEUT'