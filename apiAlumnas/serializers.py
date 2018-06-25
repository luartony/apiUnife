from rest_framework import serializers
from apiAlumnas import models

class EjemploSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Ejemplo
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class MariaAlegreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MariaAlegre
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class EdyAsteteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EdyAstete
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class JeseniaFrancoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.JeseniaFranco
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class JenniferGonzalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.JenniferGonzales
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class YaquelinHerreraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.YaquelinHerrera
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class MilagrosMagallanesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MilagrosMagallanes
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class VanessaPerezSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VanessaPerez
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class YaniraPeñaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.YaniraPeña
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')
class LadiVegaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LadiVega
        fields = ('id','created', 'title', 'url_imagen', 'likes', 'Descripción')


