from django.db import models

# Create your models here.

class Pelicula(models.Model):
	codigo = models.CharField(max_length=255)
	nombre = models.CharField(max_length=255)
	genero = models.CharField(max_length=255)
	descripcion = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

class Imagen(models.Model):
	id_pelicula = models.IntegerField()
	img = models.ImageField(upload_to="films/image")
