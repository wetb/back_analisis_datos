from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from aplicacion1.models import Boyaca

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Boyaca
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()

class FirstQSerializer(ModelSerializer):
    class Meta:
        model = Boyaca
        fields = ['MUNICIPIO','TOTAL_MATRICULA']

class SecondQSerializer(ModelSerializer):
    class Meta:
        model = Boyaca
        fields = ['GENERO','TOTAL_MATRICULA']

class ThirdQSerializer(ModelSerializer):
    class Meta:
        model = Boyaca
        fields = ['ANNO_INF','TIPO_JORNADA','TOTAL_MATRICULA']

class FourthQSerializer(ModelSerializer):
    class Meta:
        model = Boyaca
        fields = ['NOMBRE_ESTABLECIMIENTO','TOTAL_MATRICULA']

class FifthQSerializer(ModelSerializer):
    class Meta:
        model = Boyaca
        fields = ['GRADO','TOTAL_MATRICULA']

class SixthQSerializer(ModelSerializer):
    cantidad_mete= serializers.IntegerField()
    class Meta:
        model = Boyaca
        fields = ['ANNO_INF','NOMBRE_ESTABLECIMIENTO','cantidad_mete']