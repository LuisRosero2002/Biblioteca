from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Nacionalidad(models.Model):
    """ Nacionalidad """
    pais = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pais


class Autor(models.Model):
    """ Autores """
    nombre = models.CharField(max_length=50)
    nacionalidad =  models.ForeignKey('Nacionalidad', on_delete=models.PROTECT,related_name='get_pais' )
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Genero(models.Model):
    """ Genero """
    tipo = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tipo


class Libro(models.Model):
    """ Libro """
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey('Autor', on_delete=models.PROTECT,related_name='get_autor')
    genero = models.ForeignKey('Genero', on_delete=models.PROTECT,related_name='get_genero')
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo



