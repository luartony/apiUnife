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
