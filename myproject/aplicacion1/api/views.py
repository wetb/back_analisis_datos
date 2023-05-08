from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from django.forms import model_to_dict
from aplicacion1.models import Boyaca
import aplicacion1.api.serializers as serializers

class InfoApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.all()[:5]
    serializer_class = serializers.InfoSerializer

class FirstApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.filter(ANNO_INF__in=[2018, 2019]).values('MUNICIPIO').annotate(TOTAL_MATRICULA=Sum('TOTAL_MATRICULA')).order_by('-TOTAL_MATRICULA')
    serializer_class = serializers.FirstQSerializer

class SecondApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.filter(ANNO_INF__in=[2018, 2019]).values('GENERO').annotate(TOTAL_MATRICULA=Sum('TOTAL_MATRICULA'))
    serializer_class = serializers.SecondQSerializer

class ThirdApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.filter(ANNO_INF__in=[2018, 2019]).values('ANNO_INF', 'TIPO_JORNADA').annotate(TOTAL_MATRICULA=Sum('TOTAL_MATRICULA'))
    serializer_class = serializers.ThirdQSerializer

class FourthApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.filter(ANNO_INF__in=[2018, 2019]).values('NOMBRE_ESTABLECIMIENTO').annotate(TOTAL_MATRICULA=Sum('TOTAL_MATRICULA')).order_by('-TOTAL_MATRICULA')
    serializer_class = serializers.FourthQSerializer

class FifthApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.filter(ANNO_INF__in=[2018, 2019]).values('GRADO').annotate(TOTAL_MATRICULA=Sum('TOTAL_MATRICULA')).order_by('-TOTAL_MATRICULA')
    serializer_class = serializers.FifthQSerializer

class SixthApiViewSet(ModelViewSet):
    queryset = Boyaca.objects.values('ANNO_INF','NOMBRE_ESTABLECIMIENTO').annotate(cantidad_mete=Count('METODOLOGIA',distinct=True)).order_by()
    serializer_class = serializers.SixthQSerializer
