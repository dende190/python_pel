"""work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from peliculas import views as peliculas_views

urlpatterns = [
    # path('', local_views.home),

    path('', peliculas_views.home, name="home"),
    path('addFilm', peliculas_views.addFilm, name='addFilm'),
    path('film/<int:user_id>', peliculas_views.film, name='film'),
    path('film/<int:user_id>/images', peliculas_views.uploadImage, name="imagenUpload"),
    path('addImages', peliculas_views.uploadImageFilms, name="imagenUploadFilms"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
