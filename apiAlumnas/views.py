from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apiAlumnas import models
from apiAlumnas import serializers
from rest_framework import viewsets

class EjemploViewSet(viewsets.ModelViewSet):
    queryset = models.Ejemplo.objects.all()
    serializer_class = serializers.EjemploSerializer
class MariaAlegreViewSet(viewsets.ModelViewSet):
    queryset = models.MariaAlegre.objects.all()
    serializer_class = serializers.MariaAlegreSerializer
class EdyAsteteViewSet(viewsets.ModelViewSet):
    queryset = models.EdyAstete.objects.all()
    serializer_class = serializers.EdyAsteteSerializer
class JeseniaFrancoViewSet(viewsets.ModelViewSet):
    queryset = models.JeseniaFranco.objects.all()
    serializer_class = serializers.JeseniaFrancoSerializer
class JenniferGonzalesViewSet(viewsets.ModelViewSet):
    queryset = models.JenniferGonzales.objects.all()
    serializer_class = serializers.JenniferGonzalesSerializer
class YaquelinHerreraViewSet(viewsets.ModelViewSet):
    queryset = models.YaquelinHerrera.objects.all()
    serializer_class = serializers.YaquelinHerreraSerializer
class MilagrosMagallanesViewSet(viewsets.ModelViewSet):
    queryset = models.MilagrosMagallanes.objects.all()
    serializer_class = serializers.MilagrosMagallanesSerializer
class VanessaPerezViewSet(viewsets.ModelViewSet):
    queryset = models.VanessaPerez.objects.all()
    serializer_class = serializers.VanessaPerezSerializer
class YaniraPeñaViewSet(viewsets.ModelViewSet):
    queryset = models.YaniraPeña.objects.all()
    serializer_class = serializers.YaniraPeñaSerializer
class LadiVegaViewSet(viewsets.ModelViewSet):
    queryset = models.LadiVega.objects.all()
    serializer_class = serializers.LadiVegaSerializer
