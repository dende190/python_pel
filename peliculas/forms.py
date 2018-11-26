from django import forms

from peliculas.models import Imagen

class PostForm(forms.ModelForm):

	class Meta:
		model = Imagen 
		fields = ('id_pelicula', 'img')