from django.contrib import admin
from aplicacion1.models import Boyaca

# Register your models here.
@admin.register(Boyaca)
class InfoAdmin(admin.ModelAdmin):
    list_display=[
    'ANNO_INF', 
    'COD_DANE_DEPARTAMENTO',
    'DEPARTAMENTO',
    'COD_SECRETARIA',
    'SECRETARIA',
    'COD_DANE_MUNICIPIO',
    'MUNICIPIO',
    'CODIGO_DANE',
    'NOMBRE_ESTABLECIMIENTO',
    'COD_SECTOR',
    'SECTOR',
    'COD_CALENDARIO',
    'CALENDARIO',
    'CODIGO_DANE_SEDE',
    'NOMBRE_SEDE',
    'COD_ZONA',
    'ZONA',
    'COD_TIPO_JORNADA',
    'TIPO_JORNADA',
    'CODIGO_GRADO',
    'GRADO',
    'COD_METODOLOGIA',
    'METODOLOGIA',
    'COD_CARACTER',
    'CARACTER',
    'COD_ESPECIALIDAD',
    'ESPECIALIDAD',
    'EDAD',
    'COD_GENERO',
    'GENERO', 
    'COD_GRUPO_ETNICO',
    'GRUPO_ETNICO',
    'COD_SECTOR_CONPES',
    'SECTOR_CONPES',
    'TOTAL_MATRICULA']
