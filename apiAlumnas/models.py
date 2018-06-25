from django.db import models

class Ejemplo(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class MariaAlegre(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class EdyAstete(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class JeseniaFranco(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class JenniferGonzales(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class YaquelinHerrera(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class MilagrosMagallanes(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class VanessaPerez(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class YaniraPeña(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()

class LadiVega(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	url_imagen = models.ImageField(default = "default.png")
	likes = models.CharField(max_length=100, blank=True, default='0')
	Descripción = models.TextField()