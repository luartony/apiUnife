from django.db import models

class Ejemplo(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.TextField()	
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()
