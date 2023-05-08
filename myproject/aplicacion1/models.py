from django.db import models
from django.forms import model_to_dict
# # Create your models here.

class Boyaca(models.Model):
    ANNO_INF = models.IntegerField()
    COD_DANE_DEPARTAMENTO = models.IntegerField()
    DEPARTAMENTO = models.CharField(max_length=255)
    COD_SECRETARIA = models.IntegerField()
    SECRETARIA = models.CharField(max_length=255)
    COD_DANE_MUNICIPIO = models.IntegerField()
    MUNICIPIO = models.CharField(max_length=255)
    CODIGO_DANE = models.IntegerField()
    NOMBRE_ESTABLECIMIENTO = models.CharField(max_length=255)
    COD_SECTOR = models.IntegerField()
    SECTOR = models.CharField(max_length=255)
    COD_CALENDARIO = models.IntegerField()
    CALENDARIO = models.CharField(max_length=255)
    CODIGO_DANE_SEDE = models.IntegerField()
    NOMBRE_SEDE = models.CharField(max_length=255)
    COD_ZONA = models.IntegerField()
    ZONA = models.CharField(max_length=255)
    COD_TIPO_JORNADA = models.IntegerField()
    TIPO_JORNADA = models.CharField(max_length=255)
    CODIGO_GRADO = models.IntegerField()
    GRADO = models.CharField(max_length=255)
    COD_METODOLOGIA = models.IntegerField()
    METODOLOGIA = models.CharField(max_length=255)
    COD_CARACTER = models.IntegerField()
    CARACTER = models.CharField(max_length=255)
    COD_ESPECIALIDAD = models.IntegerField()
    ESPECIALIDAD = models.CharField(max_length=255)
    EDAD = models.IntegerField()
    COD_GENERO = models.IntegerField()
    GENERO = models.CharField(max_length=255)
    COD_GRUPO_ETNICO = models.IntegerField()
    GRUPO_ETNICO = models.CharField(max_length=255)
    COD_SECTOR_CONPES = models.IntegerField()
    SECTOR_CONPES = models.CharField(max_length=255)
    TOTAL_MATRICULA = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        return item
