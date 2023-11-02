from django.contrib import admin
from libros.models import Nacionalidad, Genero, Autor, Libro

# Register your models here.
admin.site.register(Nacionalidad)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Libro)
