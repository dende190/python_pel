from django.shortcuts import render, redirect
from peliculas.models import Pelicula, Imagen
from peliculas.forms import PostForm
# from django.http import HttpResponse

#controlador de vista inicial
def home(request):
	datos = Pelicula.objects.all().order_by("-id")
	return render(request, "index.html", {
			"datos": datos,
		})

#controlador de formulario para agregar peliculas
#agregar la pelicula a la base de datos
def addFilm(request):
	message = ""
	if request.method == "POST":
		codigo = request.POST["codigo"]
		name = request.POST["name"]
		desc = request.POST["desc"]
		genero = request.POST["genero"]

		agregarDatos = Pelicula.objects.create(
				codigo = request.POST["codigo"],
				nombre = request.POST["name"],
				descripcion = request.POST["desc"],
				genero = request.POST["genero"],
			)

		message = "Pelicula añadida exitosamente"

	return render(request, "addFilm.html", {
			'message': message
		})

def film(request, user_id):
	film = Pelicula.objects.get(id=user_id)
	imagen = Imagen.objects.filter(id_pelicula=user_id)

	return render(request, "film.html", {
			"datos": film,
			"imagen_film": imagen,
		})

def uploadImage(request, user_id):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("film", user_id)
		else:
			form = PostForm()

	film = Pelicula.objects.get(id=user_id)

	return render(request, "imageUpload.html", {
			'film': film,
		})

def uploadImageFilms(request):
	message = ""
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			message = "Imagen añadida exitosamente"
		else:
			form = PostForm()

	film = Pelicula.objects.all()

	return render(request, "imageUploadFilms.html", {
			'film': film,
			'message': message
		})