from django.urls import reverse_lazy
from django.views import View 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from libros.models import Nacionalidad, Genero, Autor, Libro
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Libro
from django import forms
from django.http import JsonResponse
from django.core import serializers
from libros.api_service import libroServiceAPI, AutoresServiceApi



class LibrosViews(View):
    def get(self, request):
        libro_service = libroServiceAPI()
        data = libro_service.getLibrosAPI()
        print(data)
        return render(request, 'libros/libro_list.html', {'libros': data})
    
class AutoresViews(View):
    def get(self, request):
        autor_service = AutoresServiceApi()
        data = autor_service.getAutoresAPI()
        print(data)
        return render(request, 'libros/autor_list.html', {'autores': data})
    
class AuthService(View):
    def get(self, request):
        return render(request, 'login/login.html')




# Create your views here.
class AutoresListView(ListView):
    model = Autor

class AutorDetailView(DetailView):
    model = Autor

##############################################

class LibroListView(ListView):
    model = Libro

class LibroDetailView(DetailView):
    model = Libro


####################################################
class AutorCreate(CreateView):
    model = Autor
    fields = '__all__'

class AutoresUpdate(UpdateView):
    model = Autor
    fields = '__all__' 
    template_name = ' '


class AutoresDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autores-list')

def crear_autor(request):

    if request.method == 'POST':

        nombre = request.POST.get('titulo')

        pais_id = request.POST.get('genero')  
        nacionalidad = Nacionalidad.objects.get(pk=pais_id)

        nuevo_Autor = Autor(nombre=nombre,nacionalidad=nacionalidad)
        nuevo_Autor.save()

        return redirect('autores-list')

    return render(request, 'libro_list.html')

def eliminarAutor(request,autor_id):
    libro = get_object_or_404(Libro, pk=autor_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('autores-list')

####################################################

class LibroCreate(CreateView):
    model = Libro
    fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero']


def crear_libro(request):

    if request.method == 'POST':

        titulo = request.POST.get('titulo')

        autor_id = request.POST.get('autor')  
        autor = Autor.objects.get(pk=autor_id)

        genero_id = request.POST.get('genero')  
        genero =  Genero.objects.get(pk =genero_id)

        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero)
        nuevo_libro.save()

        return redirect('libro-list')

    return render(request, 'libro_list.html')


class LibroUpdate(UpdateView):
    model = Libro
    fields = '__all__' 

def actualizar_libro(request,pk):

    libro = get_object_or_404(Libro, pk=pk)

    return JsonResponse()

class LibroDelete(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro-list')  


def eliminarLibro(request,libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro-list')
    

###################################################

def obtener_autores(request):
    autores = Autor.objects.all()
    data = serializers.serialize('json', autores)
    return JsonResponse(data, safe=False)

def obtener_generos(request):
    generos = Genero.objects.all()  
    data = serializers.serialize('json', generos)
    return JsonResponse(data, safe=False)

def obtener_paises(request):
    pais = Nacionalidad.objects.all()  
    data = serializers.serialize('json', pais)
    return JsonResponse(data, safe=False)

