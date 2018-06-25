from rest_framework import serializers
from apiAlumnas import models


class EjemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ejemplo
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')


