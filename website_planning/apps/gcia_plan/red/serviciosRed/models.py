from django.db import models


class ListPryModelo(models.Model):
    '''
    Modelo de datos que tiene guardado todos los proyectos. Se tiene
    datos propios del proyecto.
    '''
    ID = models.BigAutoField(db_column='ID', primary_key=True)
    PROYECTO_SAP = models.CharField(
        null=False,
        blank=False,
        max_length=75,
        verbose_name='Proyecto SAP',
        unique=False,
        db_column='PROYECTO_SAP')
    CEGE_UNIVERSAL = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        verbose_name='CeGe Universal',
        db_column='CEGE_UNIVERSAL')
    PROYECTO_GCIA = models.CharField(
        null=False,
        blank=False,
        max_length=75,
        verbose_name='Proyecto Gcia',
        unique=True,
        db_column='PROYECTO_GCIA')
    ESTADO = models.CharField(
        null=False,
        blank=False,
        max_length=11,
        verbose_name='Estado',
        db_column='ESTADO')
    ALCANCE = models.TextField(
        null=False,
        blank=False,
        max_length=4000,
        verbose_name='Alcance',
        db_column='ALCANCE')
    ANIO_SAP = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Anio SAP',
        db_column='ANIO_SAP')
    PAIS = models.CharField(
        null=False,
        blank=False,
        max_length=2,
        verbose_name='Pais',
        db_column='PAIS')
    RED = models.CharField(
        null=False,
        blank=False,
        max_length=5,
        verbose_name='Red',
        db_column='RED')
    VALORACION = models.CharField(
        null=False,
        blank=False,
        max_length=9,
        verbose_name='Valoracion',
        db_column='VALORACION')
    RESPONSABLE = models.CharField(
        null=False,
        blank=False,
        max_length=400,
        verbose_name='Responsable',
        db_column='RESPONSABLE')
    GERENCIA = models.CharField(
        null=False,
        blank=False,
        max_length=8,
        verbose_name='Gerencia',
        db_column='GERENCIA')
    FECHA_INICIO_ESTIMADA = models.DateField(
        null=False,
        blank=False,
        default='9999-12-31',
        verbose_name='Fecha Inicio Estimada',
        db_column='FECHA_INICIO_ESTIMADA')
    FECHA_FIN_ESTIMADA = models.DateField(
        null=False,
        blank=False,
        default='9999-12-31',
        verbose_name='Fecha Fin Estimada',
        db_column='FECHA_FIN_ESTIMADA')
    FECHA_INICIO_REAL = models.DateField(
        null=False,
        blank=True,
        default='9999-12-31',
        verbose_name='Fecha Inicio Real',
        db_column='FECHA_INICIO_REAL')
    FECHA_FIN_REAL = models.DateField(
        null=False,
        blank=True,
        default='9999-12-31',
        verbose_name='Fecha Fin Real',
        db_column='FECHA_FIN_REAL')
    FECHA_CANCELACION = models.DateField(
        null=False,
        blank=True,
        default='9999-12-31',
        verbose_name='Fecha Cancelacion',
        db_column='FECHA_CANCELACION')
    MOTIVO_CANCELACION = models.TextField(
        null=True,
        blank=True,
        max_length=4000,
        verbose_name='Motivo Cancelacion',
        db_column='MOTIVO_CANCELACION')
    USUARIO_REPORTE = models.CharField(
        blank=False,
        null=False,
        default='system',
        max_length=10,
        verbose_name='Usuario reporte',
        db_column='USUARIO_REPORTE')
    FECHA_CREACION = models.DateField(
        null=False,
        default='9999-12-31',
        # date = models.DateTimeField(default=datetime.now, blank=True)
        verbose_name='Fecha Creacion',
        db_column='FECHA_CREACION')

    class Meta:
        db_table = 'WEB_DAILYPRYCORE_LISTADO'

    def __str__(self):
        return f'{self.ID}'


class SeguiPryModelo(models.Model):
    '''Modelo del seguimiento de proyectos, status. Se tiene los 
    datos que se reportan en referencia al estado del proyecto.
    '''
    ID = models.BigAutoField(db_column='ID', primary_key=True)
    USUARIO_REPORTE = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        default='system',
        verbose_name='Usuario reporte',
        db_column='USUARIO_REPORTE')
    PROYECTO_ID = models.ForeignKey(
        ListPryModelo,
        verbose_name='ID Proyecto',
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False)
    FECHA_REPORTE = models.DateField(
        blank=False,
        null=False,
        default='9999-12-31',
        verbose_name='Fecha Reporte',
        db_column='FECHA_REPORTE')
    FASE_COMPRAS = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        verbose_name='Fase Compras',
        db_column='FASE_COMPRAS')
    FASE_PREPARACION = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        verbose_name='Fase Preparacion',
        db_column='FASE_PREPARACION')
    FASE_IMPLEMENTACION = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        verbose_name='Fase Implementacion',
        db_column='FASE_IMPLEMENTACION')
    FASE_PRUEBAS = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        verbose_name='Fase Pruebas',
        db_column='FASE_PRUEBAS')
    FASE_PRODUCCION = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        verbose_name='Fase Produccion',
        db_column='FASE_PRODUCCION')
    SITUACION = models.TextField(
        blank=False,
        null=False,
        max_length=4000,
        verbose_name='Situacion',
        db_column='SITUACION')
    FECHA_REPLAN = models.DateField(
        blank=True,
        null=False,
        default='9999-12-31',
        verbose_name='Fecha RePlan',
        db_column='FECHA_REPLAN')
    MOTIVO_REPLAN = models.TextField(
        blank=True,
        null=True,
        max_length=4000,
        verbose_name='Motivo RePlan',
        db_column='MOTIVO_REPLAN')
    FECHA_STANDBY = models.DateField(
        blank=True,
        null=False,
        default='9999-12-31',
        verbose_name='Fecha Stand By',
        db_column='FECHA_STANDBY')
    MOTIVO_STANDBY = models.TextField(
        blank=True,
        null=True,
        max_length=4000,
        verbose_name='Motivo Stand By',
        db_column='MOTIVO_STANDBY')

    class Meta:
        db_table = 'WEB_DAILYPRYCORE_SEGUIMIENTO'

    def __str__(self):
        return f'{self.ID}'


# class smcFileModel(models.Model):
#     DOC_SMC = models.FileField(upload_to='gcia_plan/red/files')

#     class Meta:
#         db_table = 'WEB_FILESMC'
