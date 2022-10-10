from django.db import models

class ListApiModelo(models.Model):
    '''
    Modelo de datos que tiene listado todas las APIs que se quieren usar y publicar, como no.
    '''
    ID = models.BigAutoField(db_column='ID', primary_key=True)
    NOMBRE = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name='Nombre',
        unique=False,
        db_column='NOMBRE')
    DESCRIPCION = models.TextField(
        null=False,
        blank=False,
        max_length=4000,
        verbose_name='Descripcion',
        db_column='DESCRIPCION')
    EJEMPLO_JSON = models.TextField(
        null=False,
        blank=False,
        max_length=5000,
        verbose_name='Ejemplo_JSON',
        db_column='EJEMPLO_JSON')
    LINK = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name='Link',
        db_column='LINK')
    PUBLICACION = models.BooleanField()

    class Meta:
        db_table = 'WEB_APIS'

    def __str__(self):
        return f'{self.ID}'